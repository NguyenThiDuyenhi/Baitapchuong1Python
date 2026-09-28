htai,rate= map(float, input().split())

sau1nam=htai*(1+rate/100)
sau2nam=sau1nam*(1+rate/100)

print(round(sau1nam), 'rồi', round(sau2nam))
