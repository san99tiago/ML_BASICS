% Access upper folder functions
addpath(genpath("../"));

ST = out.ST_02;
time = out.tout;

plot(time, ST(:, 1), time, ST(:, 2));
prettygraph("Data From Simulink", "plot");
