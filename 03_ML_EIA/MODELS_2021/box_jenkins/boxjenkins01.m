% EXECUTE BOX-JENKINS MODEL FOR TIME-SERIES
% Santiago Garcia Arango

% Clean workspace data
clear; close all; clc;

% Access upper folder functions
addpath(genpath("../"));

fprintf('Loading data....\n');
load('simulink_data_01.mat');

% Get relevant information from system's data
yd = ST(:,2); % System's response from Simulink
r = ST(:,1); % System's setpoint from Simulink 
k = 1:1:size(yd); % Vector regularly spaced starting at 1, and with increments of 1 until size(yd)

figure;
subplot(4,1,1);
plot(k,r,'r',k,yd,'b', "linewidth", 2);
hold on;
prettygraph("System's Setpoint (r) and Output (Yd)", "plot")

% Autocorrelation plots
subplot(4,1,2);
autocorr(yd, size(yd,1) - 1);
prettygraph("Sample Autocorrelation Function", "plot")

subplot(4,1,3);
parcorr(yd, 100); % Only 100 data, to avoid long-time-processing
prettygraph("Sample Partial Autocorrelation Function", "plot")


% This line is to "encapsulate" the system's input-output data and its properties...
% ... for system identification iddata(yd = output, u = input, Ts = sample time)
Ts = 0.01;
data = iddata(yd,r,Ts); % Simulation matrix for system identification


% Autoregressive Model with exogenous input (ARX)
% na --> order of polynomial A(q), Ny-by-Ny matrix of nonnegative integers
% nb --> order of polynomial B(q) + 1, Ny-by-Nu matrix of nonnegative integers
% nk --> input-output delay (transport delay), Ny-by-Nu matrix of nonnegative integers
% *** na (windows size for output) is analyzed from the autocorr of the output***
yarx = arx(data,[50,1,0]) % [na=taken_from_window_size_of_input, nb=1, nk=0]
ys1 = sim(r,yarx); % Simulate the ARX system


% Mean Average model with exogenous input (MAX)
% na --> order of polynomial A(q), Ny-by-Ny matrix of nonnegative integers
% nb --> order of polynomial B(q) + 1, Ny-by-Nu matrix of nonnegative integers
% nc --> order of the polynomial C(q), column vector of nonnegative integers of length Ny
% nk --> input-output delay (transport delay), Ny-by-Nu matrix of nonnegative integers
% *** na (windows size for output) is analyzed from the autocorr of the output***
% *** nc (delays of the error)***
ymax = armax(data,[0,1,4,0]) % [na=taken_from_window_size_of_input, nb=1, nc=4, nk=0]
ys2 = sim(r,ymax); % Simulate the MAX system


% ARMAX Model
yarmax = armax(data,[50,1,2,0])
ys3 = sim(r,yarmax); % Simulate the ARMAX system


% Only show one of the three models... (Comment the other ones)
subplot(4,1,4);
% plot(k,yd,'r',k,ys1,'b', "linewidth", 2); % ARX
% plot(k,yd,'r',k,ys2,'b', "linewidth", 2); % MAX
plot(k,yd,'r',k,ys3,'b', "linewidth", 2); % ARMAX
prettygraph("Output of real system (Yd) and output of model (Ys)", "plot")

