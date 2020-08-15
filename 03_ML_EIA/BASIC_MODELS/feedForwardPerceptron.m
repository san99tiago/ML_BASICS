% TRAIN OR TEST DATA BASED ON FEED-FORWARD-PERCEPTRON
% Santiago Garcia Arango
% ------------------------------------------------------------------------
% FEEDFORWARDPERCEPTRON. Train or Test a simple network.
%   alfa: Learning rate constante (1 x 1)
%   
%   entries: input data based on the "Xi" values (ne x nd)
%   
%   w: vector of the initial weights. size (1 x ne)
%   
%   goal: "train" to change the weights, "test" to check other values
%   
%   activation_function: "none" to pass "ys" direct.
%                        "binary" to apply ">=0" or "<0" filter.


function [yrk,ecm, w] = feedForwardPerceptron(alfa, entries, w, desired, goal, activation_function)

    nd = size(entries, 2);  % Number of Data
    ns = size(desired, 1);  % Number of Outputs

    % Additional first time variables
    yrk = zeros(ns, nd);
    ecm = zeros(ns, 1);  % Only need one to start iterating
    
    for i=1:nd
        % Main sensation output (before activation function)
        ys = w*entries(:,i);
        disp("ys:");
        disp(ys);
        
        % Apply activation function based on funciton parameters
        if activation_function == "none"
            yrk(i) = ys;
        end
        if activation_function == "binary"
            yrk(i) = (ys>=0);  % Matlab built-in function (1 or 0)
        end

        
        % Simple error and cuadratic mean error
        error = desired(i) - yrk(i);
        
        ecm(:) = ecm(:) + (error.^2)/2;
        
        if goal == "train"
            % Update weights
            w = w + alfa.*(error*entries(:,i)');
            
            disp("alfa.*(error*entries(:,i)'):")
            disp(alfa.*(error*entries(:,i)'))
            disp("w:")
            disp(w)
        end        
    end
    
end

