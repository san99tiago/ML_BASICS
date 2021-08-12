% TRAIN OR TEST DATA BASED ON FEED-FORWARD-MADALINE
% Santiago Garcia Arango
% ------------------------------------------------------------------------
% FEEDFORWARDMADALINE. Train or Test a simple neural network.
%   alfa: Learning rate constant (1 x 1)
%
%   entries: input data based on the "Xi" values (ne x nd)
%
%   W: vector of the initial Weights. size (1 x ne)
%
%   C: matrix of the initial hidden layers weights. size (ns x no+1)
%
%   desired: matrix of the desired output, based on entries size (ns x nd)
%
%   no: number of neurons in hidden layer. size (1 x 1)
%
%   ns: number of outputs. size (1 x 1)
%
%   nd: number of training data (1 x 1)
%
%   goal: "train" to change the weights, "test" to check other values
%
%   activation_function_x: "none" to pass "Ys" directly.
%                        "sigmoidal" to apply 1/(1 + exp(-value))
%                        "binary" to apply ">=0" or "<0" filter
% ------------------------------------------------------------------------


function [Yk, ecm, W, C] = feedforwardmadaline(alfa,entries, W, C, desired, no, ns, nd, goal, activation_function_1, activation_function_2)
% Start the hidden layer (remember bias is added here)
hj = zeros(no+1,1);

% Start the output (Yk) and the root-mean-square (ecm)
Yk = zeros(ns,nd);
ecm = zeros(ns,1);

for i = 1:nd
    % Find the hidden layer "aj" after initial weights and entries
    aj = W*entries(:,i);  % size (no, 1)
    
    % Add the bias to the hidden layer (before last neuron)
    hj(1) = 1;
    
    % Apply activation function to hidden layer (except bias)
    if activation_function_1 == "sigmoidal"
        hj(2:end) = 1./(1 + exp(-aj));
    end
    
    % Get output Ys after the hidden layer finds hj
    Ys = C*hj; % size (ns x 1)
    
    
    % Apply activation function to the output layer
    if activation_function_2 == "none"
        Yk(:,i) = Ys; % Linear in this case
    elseif activation_function_2 == "sigmoidal"
        Yk(:,i) = 1./(1 + exp(-Ys));
    elseif activation_function_2 == "binary"
        Yk(:,i) = (Ys>=0);
    end
    
    
    % Obtain error based on current results and add it to ecm (rms)
    error = desired(:,i) - Yk(:,i);
    ecm(:) = ecm(:) + (error.^2)./(2*nd);
    
    if goal == "train"
        
        % Find numeric derivative of "f" (sensitivity of output)
        if activation_function_2 == "none"
            % "Sensitiviity" of output layer
            ds = error; % yd - Yk
        elseif activation_function_2 == "sigmoidal"
            ds = error.*(Yk(:,i).*(1-Yk(:,i)));
        elseif activation_function_2 == "binary"
            ds = error; % yd - Yk
        end

        df1 = ((ds'*C(:,2:end)));

        % find numeric derivative of "hj" (sensitivity of hidden layer)
        if activation_function_1 == "sigmoidal"
            % We dont include the derivative of the bias (we start in "2")
            df2 = (hj(2:end).*(1 - hj(2:end)))';
            dhj = df1.*df2;
        end
                
        % Update hidden layer weights (Cjk)
        C = C + alfa*(ds*hj');

        % Update first weights (Wji)
        W = W + alfa*(dhj'*entries(:,i)');

    end
end
end
