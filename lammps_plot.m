%start1
data = readdump_all('dump190_1.lammpstrj');
t = data.timestep;
nt = length(t);
nleft = zeros(nt,1);
box = data.x_bound;
halfsize = 0.5*box(:,2);
for it = 1:nt
xit = data.atom_data(:,3,it);
jj = find(xit<halfsize(it));
nleft(it) = length(jj);
end
plot(t,nleft/data.Natoms(1)), xlabel('t'), ylabel('n/N');
yline(0.5,'--');