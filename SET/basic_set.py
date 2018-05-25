out = open('list_of_set.txt', 'w')
set = ['0','1','2','3','4','5','6','7','8','9','0']
out.write('Numbers\n{\n')
for i in set:
	out.write('%s:SET/%s\n'%(i, i))
out.write('}')
out.write('\n')

set = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
out.write('English(small)\n{\n')
for i in set:
	out.write('%s:SET/%s\n'%(i, i))
out.write('}')
out.write('\n')

set = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
out.write('English(caps)\n{\n')
for i in set:
	out.write('%s:SET/%s\n'%(i, i))
out.write('}')
out.write('\n')

set = ['?', ',', ':', ';', '!']
out.write('Punctuation\n{\n')
for i in set:
	out.write('%s:SET/%s\n'%(i, i))
out.write('}')
out.write('\n')

set = ['+', '-', '=', '<', '>']
out.write('Math\n{\n')
for i in set:
	out.write('%s:SET/%s\n'%(i, i))
out.write('}')
out.write('\n')

out.close()
