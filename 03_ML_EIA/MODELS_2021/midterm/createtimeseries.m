% SIMPLE SCRIPT TO CREATE "TIMESERIESDATA" WORKSPACE AND SAVE IT TO "TIMESERIESDATA.mat"
% Santiago Garcia Arango

N = 500;  % Total data
entries = zeros(1, N);
desired = zeros(1, N);

for i=1:N
    entries(1, i) = i;
    % function is y = cos(x^2 + 2*x^3) ... from (x=-5 to x=5)
    value = i/50 - 5;
    desired(1, i) = cos(value^2 + 2*value^3);
end

data = desired;

% Automatically save the data to the "TIMESERIESDATA.mat" workspace
save("TIMESERIESDATA.mat", "entries", "desired", "data");

figure;
plot(desired,'-b',"Linewidth",1);
xlabel('iteration');
ylabel('value');
legend('Input data', "Location", "best");
prettygraph("DATA y=cos(x^2 + 2*x^3)");

figure;
autocorr(desired, 499);
prettygraph("AUTOCORR (499)");
