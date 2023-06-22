# update:
s2 = {'ktm','hero','kawasaki','pulsar','r15','yamaha','rx100','tvsxl','apacheRTR'}

print(s2)
s2.update({'bmw','enfield'})
print(s2)
# {'ktm', 'bmw', 'kawasaki', 'tvsxl', 'r15', 'enfield', 'yamaha', 'apacheRTR', 'hero', 'pulsar', 'rx100'}


s2.update({'mastero','aprila','suziki'})
print(s2)
# {'suziki', 'yamaha', 'tvsxl', 'r15', 'hero', 'ktm', 'bmw', 'enfield', 'kawasaki', 'rx100', 'mastero', 'aprila', 'pulsar', 'apacheRTR'}



s3 = s2.copy()
print(s3)
# {'r15', 'pulsar', 'mastero', 'apacheRTR', 'kawasaki', 'ktm', 'suziki', 'bmw', 'hero', 'aprila', 'yamaha', 'enfield', 'tvsxl', 'rx100'}


s3.clear()
print(s3)
# set()


