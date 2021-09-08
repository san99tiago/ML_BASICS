% LOADING DATA "PALMS" EXECUTING MADALINE (WITH LAST LAYER AS PERCEPTRON)
% Santiago Garcia Arango

% Clean workspace data
clear; close all; clc;

% Access upper folder functions
addpath(genpath("../"));

% Load data
fprintf("...Loading database...");
load("PALMS.mat");

% -----------------------------------------------------------

% % Normalize data (to make them fit in specific (a, 1) range...
% normalizeEntriesValue = (max(max(entries)));
% entries = entries/normalizeEntriesValue;
% normalizeDesiredValue = (max(max(desired)));
% desired = desired/normalizeDesiredValue;

% Bias does not affect the first layer (only the last one)

% % Add custom entries to have more diversity of "inputs"
entries = [ones(1, size(entries,2)); entries];  % "2" is for columns
entries = [entries; sin(entries(2, :))];
entries = [entries; cos(entries(2, :))];
entries = [entries; mod(entries(2, :), 2)];

% -------------------------------------------------------------

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
no = 10;
fprintf("\t - NUMBER OF HIDDEN LAYERS (no) = %d\n", no);

% -------------------------------------------------------------

% Variables for the training of the model
alfa = 0.1;  % Training rate
nmax = 1000;  % Number of iterations
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
    [Yk, ecm(:, m), W, C] = feedforwardmadaline(alfa,entries, W, C, desired, no, ns, nd, "train", "sigmoidal", "binary");
end

% -------------------------------------------------------------

% % Revert normalization process
% Yk = Yk.*normalizeDesiredValue;
% desired = desired.*normalizeDesiredValue;

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
    prettygraph("CLIENTS MODEL MADALINE-PERCEPTRON (MSE)","plot");
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

% Plot the confusion matrix to see how each type of data was...
% Remark: ONLY if we have the "Deep Learning Toolbox"
figure;
plotconfusion(desired, Yk);
prettygraph("Confusion Matrix Results");
