% SCRIPT FOR TRAINING PERCEPTRON
% Santiago Garcia Arango

% Clean workspace data
clear; close all; clc;

% Load data
fprintf("...Loading database...");
load("AND.mat");

% Add Bias to the entries
entries = [ones(1, size(entries,2)); entries];  % "2" is for columns

% Get the important variables for the model
nd = size(entries, 2);  % Number of Data
ne = size(entries, 1);  % Number of Entries
ns = size(desired, 1);  % Number of Outputs

fprintf("THE LOADED DATABASE HAS:\n");
fprintf("\t - NUMBER OF ENTRIES (ne) = %d\n", ne);
fprintf("\t - NUMBER OF OUTPUTS (ns) = %d\n", ns);
fprintf("\t - NUMBER OF DATA (nd) = %d\n", nd);

% Variables for the training of the model
alfa = 1;  % Training rate
nmax = 10;  % Number of iterations
fprintf("\t + alfa = %d\n\t + nmax = %d\n", alfa, nmax);

% Create matrix for the initialneural network weights
% W is based on I/O of size(rows = Outputs, columns = Entries)
W = 2.*rand(ns, ne) - 1;

% Create Output matrix (rows = Outputs, columns = Data)
Yk = zeros(ns, nd);

% Create the ecm (medium cuadratic error) (rows = Outputs, columns = iterations)
ecm = zeros(ns, nmax);


% Train Neural Network
fprintf("...Training Neural Network...");

for m=1:nmax
    % Execute main feedForwardPeceptron to train or check model
    fprintf("\n-->Iteration = %d\n", m);
    [Yk, ecm(:, m), W] = feedForwardPerceptron(alfa, entries, W, desired, "train", "binary"); 
end

% Plot the ecm based on the iterations
fprintf("PLOT ECM FOR EACH OUTPUT");
for i=1:ns
    figure;
    plot(1:nmax, ecm(i,:), "b", "lineWidth", 2);
    xlabel("iteration");
    ylabel("ecm");
    legend("ECM TRAINING");
    title(strcat("OUTPUT ", num2str(i)));
    PRETTY_GRAPH("AND-GATE-MODEL","plot");
end

for i=1:ns
    fprintf('Plotting each desired-data output with the neural-net output...\n')
    figure;
    plot(1:nd,desired(i, :),'*b',1:nd,Yk(i, :),'+r',"Linewidth",2);
    xlabel('data');
    ylabel('ouput');
    legend('Desired Output','Neural Network Output', "Location", "best");
    PRETTY_GRAPH("TRAINING RESULT FOR EACH DATA");
end
