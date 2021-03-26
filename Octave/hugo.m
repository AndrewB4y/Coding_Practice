# /root/.local/bin/mh_lint hugobaymon.m 
# MISS_HIT Lint Summary: 1 file(s) analysed, everything seems fine

a = input("", "s");
b = textscan(a, "%d %d");
disp(b{1} + b{2});

# cat DATA.lst | octave hugobaymon.m
# 29266