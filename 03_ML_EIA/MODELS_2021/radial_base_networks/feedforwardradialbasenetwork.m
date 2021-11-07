% FEEDFORWARDRADIALBASENETWORK
% Santiago Garcia Arango
% ----------------------------------------
% Function that iterates through a dataset and trains a radial-base
% network.

%    This is a function that goes through the data set and trains a
%    base radial neural network.
%    :param ne: Number of entries
%    :param no: Number of classes
%    :param ns: Number of outputs
%    :param nd: Number of samples
%    :param alpha: Learning rate
%    :param entries: entries of the system
%    :param desired: Desired outputs of the system
%    :param Wkj: Neural weight matrix (Output layer)
%    :param Cji: Centers of the Gaussian Bells (Hidden layer)
%    :param Dj: Diameters of the Gaussian Bells 
%    :param train: Training flag
% ------------------------------------------

function [Yk, ecm, Cji, Wkj, Dj] = feedforwardradialbasenetwork(entries, ne, no, Cji, Dj, Wkj, desired, alpha, ns, nd, train)
    % Define important variables of the network
    Hj = zeros(no+1,1);
    Yk = zeros(ns,nd);
    ecm = zeros(ns,1);
    
    % Go through the data
    for i = 1:nd
        % Calculate some important terms
        t1 = repmat(entries(:,i),1,no) - Cji;
        dist = sum(t1.^2)';
        
        Hj(1) = 1; % Add the BIAS
        
        % Calculate the activation function (Hidden layer)
        Hj(2:end) = exp(-(dist./(2.*Dj.^2))); % Gaussian Activation function
        
        % Calculate Ak
        Ak = Wkj'*Hj;
        
        % Calculate the activation function (Output layer)
        Yk(:,i) = 1./(1+exp(-Ak));
        
        % Calculate the error 
        Ek = desired(:,i) - Yk(:,i);
        
        % Calculate the mean square error
        ecm(:) = ecm(:) + (Ek.^2)./2;
        
        if (train == 1)
            % Calculate diameters matrix
            dr = repmat(Dj,1,ne);
            
            % Train the weights of the output layer
            Wkj = Wkj + alpha.*(Hj*Ek');
            
            % Train the centers of the Gaussian Bells (Hidden layer's WS)
            Cji = Cji + repmat((alpha.*(Wkj(2:end,:)*Ek).*Hj(2:end,:))', ne, 1).*(t1./(dr'.^2));
            
            % Train the diameters of the Gaussian Bells 
            Dj = Dj + (alpha.*(Wkj(2:end,:)*Ek).*Hj(2:end,:)).*(dist./(Dj.^3));
        end
    end
end