% SCRIPT TO CREATE AND PREPARE "BINARY TO DECIMAL DECO MODEL"
% Santiago Garcia Arango
clear; close all; clc;

rng(1) % Seed to obtain same results and check

fprintf("LOADING DATABASE OF THE BIN-DEC DECO MODEL...\n");

% We load the data associated with the and-logic-gate
load("BIN_DEC.mat")

% Add Bias to the entries
entries = [ones(1, size(entries,2)); entries];  % "2" is for columns

% Get the important variables
nd = size(entries, 2);  % Number of Data
ne = size(entries, 1);  % Number of Entries
ns = size(desired, 1);  % Number of Outputs

fprintf("THE LOADED DATABASE HAS:\n");
fprintf("\t- NUMBER OF ENTRIES (ne) = %d\n", ne);
fprintf("\t- NUMBER OF OUTPUTS (ns) = %d\n", ns);
fprintf("\t- NUMBER OF DATA (nd) = %d\n", nd);

%%

nmax = 50;  % Number of iterations
alfa = 0.1;  % Training rate

% Create weight vector based on I/O (rows = Outputs, columns = Entries)
w = 2.*rand(ns, ne) - 1;

% Create Output vector (rows = Outputs, columns = Data)
yrk = zeros(ns, nd);

% Create the ecm (medium cuadratic error)
ecm = zeros(ns, nmax);

% Train the simple neural net
for m=1:nmax
    [yrk, ecm(:,m), w] = feedForwardPerceptron(alfa, entries, w, desired, "train", "none"); 
end

fprintf("WEIGHTS:\n\t");
disp(w);

% Plot the ecm based on the iterations
fprintf("PLOT ECM FOR EACH OUTPUT");
for i=1:ns
    figure;
    plot(1:nmax, ecm(i,:), "b", "lineWidth", 2);
    xlabel("iteration");
    ylabel("ecm");
    legend("ECM TRAINING");
    title(strcat("OUTPUT ", num2str(i)));
    GRAFICA_BONITA("BINARY-DECIMAL-DECO-MODEL","plot");
end

