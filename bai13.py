s1, v1, s2, v2, s3, v3 = map(float, input().split())

t1=s1/v1
t2=s2/v2
t3=s3/v3
time= t1+t2+t3
s= s1+ s2 + s3
vtb=s/time

print("Tổng", round(s), "km,", round(time), 'giờ,', 'TB', round(vtb), "km/h")
