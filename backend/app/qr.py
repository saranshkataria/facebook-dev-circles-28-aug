def qrcode(unique_id):
    import qrcode
    import base64
    from PIL import Image
    import StringIO
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Some data')
    qr.make(fit=True)
    out = StringIO.StringIO()

    img = qr.make_image()
    img.save(out,format='PNG')
    out.seek(0)
    encoded_qr_code = base64.b64encode(out.read())
    return "data:image/png;base64," + encoded_qr_code
#print qrcode("sadnbaskdj24132q4")