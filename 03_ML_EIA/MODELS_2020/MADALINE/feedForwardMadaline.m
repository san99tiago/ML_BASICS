% TRAIN OR TEST DATA BASED ON FEED-FORWARD MULTI-ADAPTIVE LINEAR ELEMENT
% Model inspired by Alejandro Puerta Echandia.
% Santiago Garcia Arango
% ------------------------------------------------------------------------
% FEEDFORWARDPERCEPTRON. Train or Test a simple network.
%   alfa: Learning rate constante (1 x 1)
%   
%   entries: input data based on the "Xi" values. size (ne x nd)
%   
%   w: matrix of the initial weights. size (no x ne)
%
%   c: matrix of the initial hidden layers weights. size (ns x no+1)
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
%   activation_function_x: "none" to pass "ys" direct.
%                        "binary" to apply ">=0" or "<0" filter.
%                        "sigmoidal" to apply 1/(1 + exp(-value))


function [yrk, ecm, w, c] = feedForwardMadaline(alfa,entries,w,c,desired,no,ns,nd,goal,activation_function_1,activation_function_2)
    % Start the hidden layer (remember bias is added here)
    h = zeros(no+1,1);
    
    % Start the output (yrk) and the root-mean-square (ecm)
    yrk = zeros(ns,nd);
    ecm = zeros(ns,1);

    for i = 1:nd
        % Find the hidden layer "aj" after initial weights and entries
        a = w*entries(:,i);  % size (no, 1)

        % Add the bias to the hidden layer (before last neuron)
        h(1) = 1;
        
        
        % Apply activation function to hidden layer (except bias)
        if activation_function_1 == "sigmoidal"
            h(2:end) = 1./(1 + exp(-a));           
        end

        
        % Get output ysk after the hidden layer finds h
        ysk = c*h; % size (ns x 1)

        
        % Apply activation function to the output layer
        if activation_function_2 == "none"
            yrk(:,i) = ysk; % Linear in this case
        end        
        if activation_function_2 == "sigmoidal"
            yrk(:,i) = 1./(1 + exp(-ysk));           
        end

        
        % Obtain error based on current results and add it to ecm (rms)
        error = desired(:,i) - yrk(:,i);
        ecm(:) = ecm(:) + (error.^2)./(2*nd);

        if goal == "train"
            
            % Find numeric derivative of "f" (sensitivity of output)
            if activation_function_2 == "none"
                ds = error; % yd - yrk
            end
            
            % find numeric derivative of "h" (sensitivity of hidden layer)
            if activation_function_1 == "sigmoidal"
                df1 = ((ds'*c(:,2:end)));
                df2 = (h(2:end).*(1 - h(2:end)))';
                dh = df1.*df2;
            end

            % Update first weights (Wji)
            w = w + alfa*(dh'*entries(:,i)');

            % Update hidden layer weights (Cjk)
            c = c + alfa*(ds*h');

        end
    end

end
