% TRAIN OR TEST DATA BASED ON FEED-FORWARD-PERCEPTRON
% Santiago Garcia Arango
% ------------------------------------------------------------------------
% FEEDFORWARDPERCEPTRON. Train or Test a simple netWork.
%   alfa: Learning rate constant (1 x 1)
%
%   entries: input data based on the "Xi" values (ne x nd)
%
%   W: vector of the initial Weights. size (1 x ne)
%
%   goal: "train" to change the Weights, "test" to check other values
%
%   activation_function: "none" to pass "ys" direct.
%                        "binary" to apply ">=0" or "<0" filter.


function [Yk, ecm, W] = feedForwardPerceptron(alfa, entries, W, desired, goal, activation_function)

% Detect important variables from entries and desired matrices
nd = size(entries, 2);  % Number of Data
ns = size(desired, 1);  % Number of Outputs

% Additional first time variables
Yk = zeros(ns, nd);
ecm = zeros(ns, 1);  % Only need one to start iterating

% We must execute the iteration for all data...
for i=1:nd
    % Main sensation output ("Agregations" Aj) (before activation function)
    ys = W*entries(:,i);  % Also named "Aj"
    disp("ys:");
    disp(ys);
    
    % Apply activation function based on function parameters
    if activation_function == "none"
        Yk(:, i) = ys;
    end
    if activation_function == "binary"
        Yk(:, i) = (ys>=0);  % Matlab built-in function (1 or 0)
    end
    
    % Simple error and root mean square error
    error = desired(:, i) - Yk(:, i);
    ecm(:) = ecm(:) + (error.^2)/2;
    
    if goal == "train"
        % Update Weights only when the goal is to train...
        W = W + alfa.*(error*entries(:,i)');
        
        fprintf("alfa.*(error*entries(:,%d)'):\n", i)
        disp(alfa.*(error*entries(:,i)'))
        fprintf("W on iteration %d:\n", i)
        disp(W)
    end
end

end

