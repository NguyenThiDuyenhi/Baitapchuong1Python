dongia, sl, giam, vat= map(float, input().split())

sau_giamgia = dongia*sl*(1-giam/100)
thanhtoan= sau_giamgia*(1+vat/100)

print("Thanh toán: " , f'{thanhtoan:,.0f}', 'đ')
