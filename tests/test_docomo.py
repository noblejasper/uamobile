# -*- coding: utf-8 -*-
from tests import msg, MockWSGIEnviron as Environ
from uamobile import detect

def test_useragent_docomo():
    def inner(useragent, version, html_version, model, cache_size,
              is_foma, vendor, series, options=None):

        ua = detect(Environ(useragent))
        assert ua.is_docomo()
        assert ua.is_ezweb() == False
        assert ua.is_softbank() == False
        assert ua.is_vodafone() == False
        assert ua.is_jphone() == False
        assert ua.is_willcom() == False
        assert ua.is_nonmobile() == False, ua

        assert ua.html_version == html_version, msg(ua, ua.html_version, html_version)
        assert ua.model == model, (ua, model)
        assert ua.cache_size == cache_size, (ua, cache_size)
        assert ua.is_foma() == is_foma, (ua, is_foma)
        assert ua.vendor == vendor, (ua, vendor)
        assert ua.series == series, msg(ua, ua.series, series)

        if options:
            for k, v in options.items():
                if k == 'status':
                    assert ua.status == v, msg(ua, ua.status, v)
                elif k == 'serial_number':
                    assert ua.serialnumber == v, msg(ua, ua.serialnumber, v)
                elif k == 'card_id':
                    assert ua.card_id == v, msg(ua, ua.card_id, v)
                elif k == 'bandwidth':
                    assert ua.bandwidth == v, msg(ua, ua.bandwidth, v)
                elif k == 'comment':
                    assert ua.comment == v, msg(ua, ua.comment, v)
                elif k == 'is_gps':
                    assert ua.is_gps() == v, msg(ua, ua.is_gps(), v)

    for args in DATA:
        yield ([inner] + list(args))

#########################
# Test data
#########################

DATA = (
# ua, version, html_version, model, cache_size, is_foma, vendor, series, options
('DoCoMo/1.0/D501i', '1.0', '1.0', 'D501i', 5, False, 'D', '501i'),
('DoCoMo/1.0/D502i', '1.0', '2.0', 'D502i', 5, False, 'D', '502i'),
('DoCoMo/1.0/D502i/c10', '1.0', '2.0', 'D502i', 10, False, 'D', '502i'),
('DoCoMo/1.0/D210i/c10', '1.0', '3.0', 'D210i', 10, False, 'D', '210i'),
('DoCoMo/1.0/SO503i/c10', '1.0', '3.0', 'SO503i', 10, False, 'SO', '503i'),
('DoCoMo/1.0/D211i/c10', '1.0', '3.0', 'D211i', 10, False, 'D', '211i'),
('DoCoMo/1.0/SH251i/c10', '1.0', '3.0', 'SH251i', 10, False, 'SH', '251i'),
('DoCoMo/1.0/R692i/c10', '1.0', '3.0', 'R692i', 10, False, 'R', '692i'),
('DoCoMo/2.0 P2101V(c100)', '2.0', '3.0', 'P2101V', 100, True, 'P', 'FOMA'),
('DoCoMo/2.0 N2001(c10)', '2.0', '3.0', 'N2001', 10, True, 'N', 'FOMA'),
               ('DoCoMo/2.0 N2002(c100)', '2.0', '3.0', 'N2002', 100, True, 'N', 'FOMA'),
               ('DoCoMo/2.0 D2101V(c100)', '2.0', '3.0', 'D2101V', 100, True, 'D', 'FOMA'),
               ('DoCoMo/2.0 P2002(c100)', '2.0', '3.0', 'P2002', 100, True, 'P', 'FOMA'),
               ('DoCoMo/2.0 MST_v_SH2101V(c100)', '2.0', '3.0', 'SH2101V', 100, True, 'SH', 'FOMA'),
               ('DoCoMo/2.0 T2101V(c100)', '2.0', '3.0', 'T2101V', 100, True, 'T', 'FOMA'),
               ('DoCoMo/1.0/D504i/c10', '1.0', '4.0', 'D504i', 10, False, 'D', '504i'),
               ('DoCoMo/1.0/D504i/c30/TD', '1.0', '4.0', 'D504i', 30, False, 'D', '504i', { 'status':'TD' }),
               ('DoCoMo/1.0/D504i/c10/TJ', '1.0', '4.0', 'D504i', 10, False, 'D', '504i', { 'status':'TJ' }),
               ('DoCoMo/1.0/F504i/c10/TB', '1.0', '4.0', 'F504i', 10, False, 'F', '504i', { 'status':'TB' }),
               ('DoCoMo/1.0/D251i/c10', '1.0', '4.0', 'D251i', 10, False, 'D', '251i'),
               ('DoCoMo/1.0/F251i/c10/TB', '1.0', '4.0', 'F251i', 10, False, 'F', '251i', { 'status':'TB' }),
               ('DoCoMo/1.0/F671iS/c10/TB', '1.0', '4.0', 'F671iS', 10, False, 'F', '671i', {'status':'TB'}),
('DoCoMo/1.0/P503i/c10/serNMABH200331', '1.0', '3.0', 'P503i', 10, False, 'P', '503i', {'serial_number':'NMABH200331' }),
('DoCoMo/2.0 N2001(c10;ser0123456789abcde;icc01234567890123456789)', '2.0', '3.0', 'N2001', 10, 1, 'N', 'FOMA', {'serial_number':'0123456789abcde', 'card_id' :'01234567890123456789'}),
               ('DoCoMo/1.0/eggy/c300/s32/kPHS-K', '1.0', '3.2', 'eggy', 300, False, None, None, {'bandwidth' : 32 }),
               ('DoCoMo/1.0/P751v/c100/s64/kPHS-K', '1.0', '3.2', 'P751v', 100, False, 'P', None, {'bandwidth' :64}),
               ('DoCoMo/1.0/P209is (Google CHTML Proxy/1.0)', '1.0', '2.0', 'P209is', 5, False, 'P', '209i', {'comment' :'Google CHTML Proxy/1.0'}),
               ('DoCoMo/1.0/F212i/c10/TB', '1.0', '4.0', 'F212i', 10, False, 'F', '212i', { 'status':'TB' }),
               ('DoCoMo/2.0 F2051(c100;TB)', '2.0', '4.0', 'F2051', 100, True, 'F', 'FOMA', { 'status':'TB' }),
               ('DoCoMo/2.0 N2051(c100;TB)', '2.0', '4.0', 'N2051', 100, True, 'N', 'FOMA', { 'status':'TB' }),
               ('DoCoMo/2.0 P2102V(c100;TB)', '2.0', '4.0', 'P2102V', 100, True, 'P', 'FOMA', { 'status':'TB' }),
               ('DoCoMo/1.0/N211iS/c10', '1.0', '3.0', 'N211iS', 10, False, 'N', '211i'),
               ('DoCoMo/1.0/P211iS/c10', '1.0', '3.0', 'P211iS', 10, False, 'P', '211i'),
               ('DoCoMo/1.0/N251iS/c10/TB', '1.0', '4.0', 'N251iS', 10, False, 'N', '251i', { 'status':'TB' }),
               ('DoCoMo/1.0/F661i/c10/TB', '1.0', '4.0', 'F661i', 10, False, 'F', '661i', {'status' :'TB', 'is_gps' :True}),
               ('DoCoMo/1.0/D505i/c20/TC/W20H10', '1.0', '5.0', 'D505i', 20, False, 'D', '505i', { 'status':'TC' }),
               ('DoCoMo/1.0/SO505i/c20/TB/W21H09', '1.0', '5.0', 'SO505i', 20, False, 'SO', '505i', { 'status':'TB' }),
               ('DoCoMo/2.0 N2701(c100;TB)', '2.0', '4.0', 'N2701', 100, True, 'N', 'FOMA', { 'status':'TB' }),
               ('DoCoMo/1.0/SH505i/c20/TB/W24H12', '1.0', '5.0', 'SH505i', 20, False, 'SH', '505i', { 'status':'TB' }),
               ('DoCoMo/1.0/N505i/c20/TB/W20H10', '1.0', '5.0', 'N505i', 20, False, 'N', '505i', { 'status':'TB' }),
('DoCoMo/2.0 F2102V(c100;TB)', '2.0', '4.0', 'F2102V', 100, True, 'F', 'FOMA', { 'status':'TB' }),
('DoCoMo/2.0 N2102V(c100;TB)', '2.0', '4.0', 'N2102V', 100, True, 'N', 'FOMA', { 'status':'TB' }),
('DoCoMo/1.0/F505i/c20/TB/W20H10', '1.0', '5.0', 'F505i', 20, False, 'F', '505i', { 'status':'TB' }),
('DoCoMo/1.0/P505i/c20/TB/W20H10', '1.0', '5.0', 'P505i', 20, False, 'P', '505i', { 'status':'TB' }),
('DoCoMo/1.0/F672i/c10/TB', '1.0', '4.0', 'F672i', 10, False, 'F', '672i', { 'status':'TB' }),
('DoCoMo/1.0/SH505i2/c20/TB/W24H12', '1.0', '5.0', 'SH505i', 20, False, 'SH', '505i', { 'status':'TB' }),
               ('DoCoMo/1.0/D252i/c10/TB/W25H12', '1.0', '5.0', 'D252i', 10, False, 'D', '252i', { 'status':'TB' }),
               ('DoCoMo/1.0/SH252i/c20/TB/W24H12', '1.0', '5.0', 'SH252i', 20, False, 'SH', '252i', { 'status':'TB' }),
               ('DoCoMo/1.0/D505iS/c20/TB/W20H10', '1.0', '5.0', 'D505iS', 20, False, 'D', '505i', { 'status':'TB' }),
('DoCoMo/1.0/P505iS/c20/TB/W20H10', '1.0', '5.0', 'P505iS', 20, False, 'P', '505i', { 'status':'TB' }),
('DoCoMo/1.0/P252i/c10/TB/W22H10', '1.0', '5.0', 'P252i', 10, False, 'P', '252i', { 'status':'TB' }),
('DoCoMo/1.0/N252i/c10/TB/W22H10', '1.0', '5.0', 'N252i', 10, False, 'N', '252i', { 'status':'TB' }),
('DoCoMo/1.0/N505iS/c20/TB/W20H10', '1.0', '5.0', 'N505iS', 20, False, 'N', '505i', { 'status':'TB' }),
('DoCoMo/1.0/SO505iS/c20/TB/W20H10', '1.0', '5.0', 'SO505iS', 20, False, 'SO', '505i', { 'status':'TB' }),
('DoCoMo/1.0/SH505iS/c20/TB/W24H12', '1.0', '5.0', 'SH505iS', 20, False, 'SH', '505i', { 'status':'TB' }),
('DoCoMo/1.0/F505iGPS/c20/TB/W20H10', '1.0', '5.0', 'F505iGPS', 20, False, 'F', '505i', { 'status':'TB' }),
('DoCoMo/2.0 F900i(c100;TB;W22H12)', '2.0', '5.0', 'F900i', 100, True, 'F', '900i', { 'status':'TB' }),
('DoCoMo/2.0 N900i(c100;TB;W24H12)', '2.0', '5.0', 'N900i', 100, True, 'N', '900i', { 'status':'TB' }),
('DoCoMo/2.0 P900i(c100;TB;W24H11)', '2.0', '5.0', 'P900i', 100, True, 'P', '900i', { 'status':'TB' }),
('DoCoMo/2.0 SH900i(c100;TB;W24H12)', '2.0', '5.0', 'SH900i', 100, True, 'SH', '900i', { 'status':'TB' }),
('DoCoMo/1.0/D506i/c20/TB/W20H10', '1.0', '5.0', 'D506i', 20, False, 'D', '506i', { 'status':'TB' }),
('DoCoMo/1.0/P651ps', '1.0', '2.0', 'P651ps', 5, False, 'P', '651'),
('DoCoMo/1.0/SO213i/c10/TB', '1.0', '4.0', 'SO213i', 10, False, 'SO', '213i', { 'status':'TB' }),
('DoCoMo/2.0 F880iES(c100;TB;W20H08)', '2.0', '5.0', 'F880iES', 100, True, 'F', '880i', { 'status':'TB' }),
('DoCoMo/1.0/SO213iS/c10/TB', '1.0', '4.0', 'SO213iS', 10, False, 'SO', '213i', { 'status':'TB' }),
('DoCoMo/1.0/P253i/c10/TB/W22H10', '1.0', '5.0', 'P253i', 10, False, 'P', '253i', { 'status':'TB' }),
('DoCoMo/1.0/P213i/c10/TB/W22H10', '1.0', '5.0', 'P213i', 10, False, 'P', '213i', { 'status':'TB' }),
('DoCoMo/2.0 N900iG(c100;TB;W24H12)', '2.0', '5.0', 'N900iG', 100, True, 'N', '900i', { 'status':'TB' }),
('DoCoMo/2.0 F901iC(c100;TB;W23H12)', '2.0', '5.0', 'F901iC', 100, True, 'F', '901i', { 'status':'TB' }),
('DoCoMo/1.0/SO506iS/c20/TB/W20H10', '1.0', '5.0', 'SO506iS', 20, False, 'SO', '506i', { 'status':'TB' }),
('DoCoMo/2.0 SH901iS(c100;TB;W24H12)', '2.0', '5.0', 'SH901iS', 100, True, 'SH', '901i', { 'status':'TB' }),
('DoCoMo/2.0 F901iS(c100;TB;W23H12)', '2.0', '5.0', 'F901iS', 100, True, 'F', '901i', { 'status':'TB' }),
('DoCoMo/2.0 D901iS(c100;TB;W23H12)', '2.0', '5.0', 'D901iS', 100, True, 'D', '901i', { 'status':'TB' }),
('DoCoMo/2.0 P901iS(c100;TB;W24H12)', '2.0', '5.0', 'P901iS', 100, True, 'P', '901i', { 'status':'TB' }),
('DoCoMo/2.0 N901iS(c100;TB;W24H12)', '2.0', '5.0', 'N901iS', 100, True, 'N', '901i', { 'status':'TB' }),
('DoCoMo/2.0 SH851i(c100;TB;W24H12)', '2.0', '5.0', 'SH851i', 100, True, 'SH', '851i', { 'status':'TB' }),
('DoCoMo/1.0/SO213iWR/c10/TB', '1.0', '4.0', 'SO213iWR', 10, False, 'SO', '213i', { 'status':'TB' }),
('DoCoMo/2.0 SA700iS(c100;TB;W24H12)', '2.0', '5.0', 'SA700iS', 100, True, 'SA', '700i', { 'status':'TB' }),
('DoCoMo/2.0 P851i(c100;TB;W24H12)', '2.0', '5.0', 'P851i', 100, True, 'P', '851i', { 'status':'TB' }),
('DoCoMo/2.0 D701iWM(c100;TB;W23H12)', '2.0', '5.0', 'D701iWM', 100, True, 'D', '701i', { 'status':'TB' }),
('DoCoMo/2.0 SH902i(c100;TB;W24H12)', '2.0', '6.0', 'SH902i', 100, True, 'SH', '902i', { 'status':'TB' }),
('DoCoMo/2.0 NM850iG(c100;TB;W22H10;ser000000000000000;icc)', '2.0', '4.0', 'NM850iG', 100, True, 'NM', '850i', { 'status':'TB' }),
('DoCoMo/2.0 N703imyu(c100;TB;W24H12)', '2.0', '7.0', 'N703imyu', 100, True, 'N', '703i', { 'status':'TB' }),
('DoCoMo/2.0 P703imyu(c100;TB;W24H12)', '2.0', '6.0', 'P703imyu', 100, True, 'P', '703i', { 'status':'TB' })
)
