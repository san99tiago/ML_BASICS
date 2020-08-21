%% MULTIADAPTIVE LINEAR ELEMENT (MADALINE)
% SANTIAGO GARCIA ARANGO
clear ; close all; clc;

%% PART 1: Load data and normalize it properly

fprintf('Loading entry-data and desired-data...\n')
load('BIN_DEC.mat');

% Normalize the entries and the desired values to a range of (-1,1)
max_entries = max(max(entries));
min_entries = min(min(entries));
max_desired = max(max(desired));
min_desired = min(min(desired));
entries = (entries - min_entries)/(max_entries - min_entries);
desired = (desired - min_desired)/(max_desired - min_desired);

% Obtengo el número de datos, número de entradas y número de salidas.
nd = size(entries,2);
ne = size(entries,1);
ns = size(desired,1);

% Show general information of loaded data
fprintf('Loaded data has...\n');
fprintf('\t- Number of entries (ne) = %d\n',ne);
fprintf('\t- Number of outputs (ns) = %d\n',ns);
fprintf('\t- Number of training data (nd) = %d\n',nd);


%% PART 2: Setting and initialzing the network

% Ask the user for alfa, no, nmax
% alfa = input('\nEntry the learning rate (alfa):\n');
% no = input('Entry the number of inner neurons in the hidden layer (no):\n');
% nmax = input('Entry the max iterations of the algorithm (nmax):\n');
alfa = 0.1;
no = 2;
nmax = 1000;

% Setup the initial weights (Wji and Cjk)
w = 2.*rand(no,ne) - 1;
c = 2.*rand(ns,no+1) - 1;  % Notice that the "no+1" is because of bias.

% Initialize the yrk (main network output) and ecm(root mean square)
yrk = zeros(ns,nd);
ecm = zeros(ns,nmax);


%% PART 3: FEED-FORWARD OF NEURAL NETWORK
fprintf('Starting the training of neural network...\n')

for m = 1:nmax
   [yrk, ecm(:,m),w,c] = feedForwardMadaline(alfa,entries,w,c,desired,no,ns,nd,"train","sigmoidal","none");
   
end

fprintf('Plotting the Root Mean Square (ecm) ...\n')
for i = 1:ns
    figure;
    plot(1:nmax,ecm(i,:),'b',"Linewidth",2);
    xlabel('iteration');
    ylabel('ecm');
    legend('ecm training')
    GRAFICA_BONITA("ROOT MEAN SQUARE ANALYSIS", "plot");
end

fprintf('Plotting each desired-data output with the neural-net output...\n')
figure;
plot(1:nd,desired,'b',1:nd,yrk,'+r',"Linewidth",2);
xlabel('data');
ylabel('ouput');
legend('Desired Output','Neural Network Output', "Location", "best");
GRAFICA_BONITA("TRAINING RESULT FOR EACH DATA");
