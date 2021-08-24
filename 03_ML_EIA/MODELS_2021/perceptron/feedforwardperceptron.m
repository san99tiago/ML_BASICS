% TRAIN OR TEST DATA BASED ON FEED-FORWARD-PERCEPTRON
% Santiago Garcia Arango
% ------------------------------------------------------------------------
% FEEDFORWARDPERCEPTRON. Train or Test a simple neural network.
%   alfa: Learning rate constant (1 x 1)
%
%   entries: input data based on the "Xi" values (ne x nd)
%
%   W: vector of the initial Weights. size (1 x ne)
%
%   goal: "train" to change the Weights, "test" to check other values
%
%   activation_function: "none" to pass "Ys" direct. (NOT a Perceptron)
%                        "binary" to apply ">=0" or "<0" (Real Perceptron)
% ------------------------------------------------------------------------


function [Yk, ecm, W] = feedforwardperceptron(alfa, entries, W, desired, goal, activation_function)

% Detect important variables from entries and desired matrices
nd = size(entries, 2);  % Number of Data
ns = size(desired, 1);  % Number of Outputs

% Additional first time variables
Yk = zeros(ns, nd);
ecm = zeros(ns, 1);  % Only need one to start iterating

% We must execute the iteration for all data...
for i=1:nd
    % Main sensation output ("Agregations" Aj) (before activation function)
    Ys = W*entries(:,i);  % Also named "Aj"
    fprintf("Ys on internal iteration %d:\n", i);
    disp(Ys);
    
    % Apply activation function based on function parameters
    if activation_function == "none"
        Yk(:, i) = Ys;
    end
    if activation_function == "binary"
        Yk(:, i) = (Ys>=0);  % Matlab built-in function (1 or 0)
    end
    
    fprintf("Yk(:, %d):\n", i);
    disp(Yk(:, i));
    
    % Simple error and mean square error
    error = desired(:, i) - Yk(:, i);
    ecm(:) = ecm(:) + (error.^2)/2
    
    if goal == "train"
        % Update Weights only when the goal is to train...
        W = W + alfa.*(error*entries(:,i)');
        
        fprintf("alfa.*(error*entries(:,%d)'):\n", i)
        disp(alfa.*(error*entries(:,i)'))
        fprintf("W on internal iteration %d:\n", i)
        disp(W)
    end
end

end

