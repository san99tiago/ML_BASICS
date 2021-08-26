% SAMPLE SCRIPT TO LOAD AND PLAY WITH A TIME SERIES
% SANTIAGO GARCIA ARANGO

% Clean workspace data
clear; close all; clc;

% Access upper folder functions
addpath(genpath("../"));

% Load data
fprintf("...Loading database...\n");
load("time_series02.mat");

% Important variables for time-series
windowSize = 4;
H = 20;


% Create entries based on data
entries = zeros(windowSize, size(data, 2) - windowSize + 1);

for i=1:windowSize
    currentValue=i;
    for j=1:size(data, 2)-windowSize+1
        entries(i, j) = currentValue;
        currentValue = currentValue + 1;
    end
end

desired = zeros(1, size(data, 2)-windowSize+1);
for j=1:size(data, 2)-windowSize+1
    desired(1, j) = data(1, j+windowSize-1);
end

% ------------------------------------------------------------------
% EXECUTE MADALINE

% Normalize data (to make them fit in specific (a, 1) range...
normalizeEntriesValue = (max(max(entries)));
entries = entries/normalizeEntriesValue;
normalizeDesiredValue = (max(max(desired)));
desired = desired/normalizeDesiredValue;

% Get the important variables for the model
nd = size(entries, 2);  % Number of Data
ne = size(entries, 1);  % Number of Entries
ns = size(desired, 1);  % Number of Outputs

fprintf("THE LOADED DATABASE HAS:\n");
fprintf("\t - NUMBER OF ENTRIES (ne) = %d\n", ne);
fprintf("\t - NUMBER OF OUTPUTS (ns) = %d\n", ns);
fprintf("\t - NUMBER OF DATA (nd) = %d\n", nd);

% -------------------------------------------------------------

% Get total of hidden layers (no)
no = 20;
fprintf("\t - NUMBER OF HIDDEN LAYERS (no) = %d\n", no);

% -------------------------------------------------------------

% Variables for the training of the model
alfa = 0.1;  % Training rate
nmax = 500;  % Number of iterations
fprintf("\t + alfa = %d\n\t + nmax = %d\n", alfa, nmax);

% -------------------------------------------------------------

% Create matrix for the initialneural network weights
% W is based on I/O of size(rows = Hidden Layers, columns = Entries)
% C is based on I/O of size(rows = Outputs, columns = Hidden Layers + 1)
W = 2.*rand(no, ne) - 1;
C = 2.*rand(ns,no+1) - 1;  % Notice that the "no+1" is because of bias.

% Create Output matrix (rows = Outputs, columns = Data)
Yk = zeros(ns, nd);

% Create the ecm (medium cuadratic error) (rows = Outputs, columns = iterations)
ecm = zeros(ns, nmax);

% Train Neural Network
fprintf("...Training Neural Network...");

for m=1:nmax
    % Execute main feedfowardadaline to train or check model
    fprintf("\n-->Iteration = %d\n", m);
    [Yk, ecm(:, m), W, C] = feedforwardmadaline(alfa,entries, W, C, desired, no, ns, nd, "train", "sigmoidal", "none");
end

% -------------------------------------------------------------

% Revert normalization process
Yk = Yk.*normalizeDesiredValue;
desired = desired.*normalizeDesiredValue;

% -------------------------------------------------------------

% Plot the ecm based on the iterations
fprintf("PLOT ECM FOR EACH OUTPUT");
for i=1:ns
    figure;
    plot(1:nmax, ecm(i,:), "b", "lineWidth", 2);
    xlabel("iteration");
    ylabel("ecm");
    legend("ECM TRAINING");
    title(strcat("OUTPUT ", num2str(i)));
    prettygraph("DEC-BIN MODEL MADALINE-PERCEPTRON (MSE)","plot");
end

for i=1:ns
    fprintf('Plotting each desired-data output with the neural-net output...\n')
    figure;
    plot(1:nd,desired(i, :),'*b',1:nd,Yk(i, :),'+r',"Linewidth",1);
    xlabel('data');
    ylabel('ouput');
    legend('Desired Output','Neural Network Output', "Location", "best");
    prettygraph("TRAINING RESULTS FOR EACH DATA");

end


% ------------------------------------------------------------------------
% ------------------------------------------------------------------------
% Validate time-series output with prediction of neural network

% Create entries based on data
newentriesfortest = zeros(windowSize, size(data, 2) - windowSize + 1);

for i=1:windowSize
    currentValue = i + size(data, 2) - windowSize + 1;
    for j=1:size(data, 2)-windowSize+1
        newentriesfortest(i, j) = currentValue;
        currentValue = currentValue + 1;
    end
end

% Normalize data (to make them fit in specific (a, 1) range...
newentriesfortest = newentriesfortest/normalizeEntriesValue;

% Create Output matrix (rows = Outputs, columns = Data)
Yk = zeros(ns, nd);

% Create the ecm (medium cuadratic error) (rows = Outputs, columns = iterations)
ecm = zeros(ns, nmax);

% Train Neural Network
fprintf("...Training Neural Network...");

for m=1:nmax
    % Execute main feedfowardadaline to train or check model
    fprintf("\n-->Iteration = %d\n", m);
    [Yk, ecm(:, m), W, C] = feedforwardmadaline(alfa,newentriesfortest, W, C, desired, no, ns, nd, "validate", "sigmoidal", "none");
end

% -------------------------------------------------------------

% Revert normalization process
Yk = Yk.*normalizeDesiredValue;

% -------------------------------------------------------------

% Segment outputs for only the desired horizon)
Yk = Yk(1:H + 1);

for i=1:ns
    figure;
    plot(1:nd,desired(i, :),'*b',nd+1:nd+1+H,Yk(i, :),'+r',"Linewidth",1);
    xlabel('data');
    ylabel('ouput');
    legend('Measured Data', 'Predicted Data', "Location", "best");
    prettygraph("TRAINING RESULTS ANALYSIS");
end

