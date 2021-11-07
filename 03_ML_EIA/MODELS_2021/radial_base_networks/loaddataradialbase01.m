% LOAD AND TRAIN RADIAL-BASED NEURAL NETWORK
% Santiago Garcia Arango

% Clean up the Matlab workspace
clear ; close all; clc

% Access upper folder functions
addpath(genpath("../"));

% Load the database
fprintf('Loading entries and the desired...\n')
load('data_iris.mat');

% Normalize the dataset
maxdesired = max(max(abs(desired)));
entries = entries/max(max(abs(entries)));
desired = desired/maxdesired;

% Analyze the database
nd = size(entries,2);
ne = size(entries,1);
ns = size(desired,1);

% Show the info to the user 
fprintf('The features of the loaded dataset are:\n');
fprintf('\t- Number of entries = %d\n',ne);
fprintf('\t- Number of outputs = %d\n',ns);
fprintf('\t- Number of samples = %d\n\n',nd);


% Ask the number of hidden to the user
no = input("Enter the number of classes: \n");
fprintf("OK...\n");

% Ask alpha to the user
alpha = input("Enter alpha: \n");
fprintf("OK...\n");

% Ask the number of iterations to the user
nit = input("Enter the number of iterations: \n");
fprintf("OK...\n");

% Define the centers of the Gaussian Bells Cji
C = 2*rand(ne,no)-1;

% Define the diameters of the Gaussian Bells Dj.
D = rand(no,1)./1;

% Define the weights of the output layer
W = 2.*rand(no+1,ns) - 1;

% Create output vector
Yk = zeros(ns,nd);

% Create the mean square error's matrix 
ecm = zeros(ns,nit);

% The network training begin
fprintf('Training...\n')
for m = 1:nit
   [Yk, ecm(:,m), C, W, D] = feedforwardradialbasenetwork(entries,ne,no,C,D,W,desired,alpha,ns,nd,1);
   
   if (mod(m,50)==0)
        fprintf('Iteration %d: \n',m);
   end
end

% Unnormalize the Yk
Yk = Yk.*maxdesired;
  
fprintf('Plotting Mean Square Errors ...\n')
for i = 1:ns
    figure;
    plot(1:nit,ecm(i,:),'b');
    xlabel('Iteration');
    ylabel('mse');
    legend('mse trained')
    prettygraph("Training results for each data");
end

figure;
fprintf('Plot of the confution matrix for the trained data...\n')
plotconfusion(desired,Yk,'Training');
prettygraph("Confusion Matrix Results");
