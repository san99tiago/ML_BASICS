% TRAIN OR TEST DATA BASED ON FEED-FORWARD-PERCEPTRON
% Santiago Garcia Arango

function [yrk,ecm, w] = feedForwardPerceptron(alfa, entries, w, desired, goal)
%FEEDFORWARDPERCEPTRON Summary of this function goes here
%   Train or Test a simple neural network based on shown parameters
    nd = size(entries, 2);  % Number of Data
    ns = size(desired, 1);  % Number of Outputs

    % Additional first time variables
    yrk = zeros(ns, nd);
    ecm = zeros(ns, 1);  % Only need one to start iterating
    
    for i=1:nd
        % Main sensation output (before activation function)
        ys = w*entries(:,i);
        
        % Apply activation function
        yrk(i) = (ys>=0);  % Matlab built-in function (1 or 0)
        
        % Simple error and cuadratic mean error
        error = desired(i) - yrk(i);
        ecm(:) = ecm(:) + (error.^2)/2;
        
        if goal == "train"
            % Update weights
            w = w + alfa.*(error*entries(:,i)');
        end        
    end
    
end

