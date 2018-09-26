from asn1_codecs import TestSchema


octstr = TestSchema.OctetString

with open('encoded_16384_len_payload.per') as f:
    data = f.read()

pycrate_data = octstr.to_aper(16384 * '\x05')

print 'Are ASN.1 Playground and pycrate encoded data equal?: {}'.format(data == pycrate_data)

print 'Decoding ASN.1 Playground data...'
octstr.from_aper(data)
