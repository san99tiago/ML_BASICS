% SIMPLE SCRIPT TO FIND THE DERIVATIVE OF AN ACTIVATION FUNCTION
% Santiago Garcia Arango

clc; clear variables; 

syms A B C D x

fun_1 = A*exp(-B*x^2)
fun_2 = C*exp(-D*x^2)

derivative_1 = simplify(diff(fun_1, x));
pretty(expand(derivative_1))

derivative_2 = simplify(diff(fun_2, x));
pretty(expand(derivative_2))
