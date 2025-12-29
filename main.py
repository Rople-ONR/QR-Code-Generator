from urllib.parse import urlparse
import qrcode
import os

url = ""

with open('URL_List.txt', 'r', encoding= "utf-8") as url_list_file:
    for line in url_list_file:
        url = line.strip()
        if not url: continue

        parse_url = urlparse(url)

        if not parse_url.netloc:
            parsed = urlparse("https://" + url)
            full_url = "https://" + url if parsed.netloc else url
        else:
            full_url = url

        parse_url = urlparse(full_url)
        site_name = parse_url.netloc.split('.')

        if len(site_name) >= 2:
            main_name = site_name[-2]
        else:
            main_name = "unknown"
        
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border=4
        )
        qr.add_data(full_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color = "white")
        os.makedirs('generated_qr', exist_ok=True)
        img.save(os.path.join('generated_qr', f'{main_name}.png'))
        
        print(f'{main_name} QR코드 저장 성공')