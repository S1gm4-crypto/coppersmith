from sage.all import*
from Crypto.Util.number import*
import sys
#sys.path.append("coppersmith")
from coppersmith_multivariate_heuristic import coppersmith_multivariate_heuristic
n = 13588728652719624755959883276683763133718032506385075564663911572182122683301137849695983901955409352570565954387309667773401321714456342417045969608223003274884588192404087467681912193490842964059556524020070120310323930195454952260589778875740130941386109889075203869687321923491643408665507068588775784988078288075734265698139186318796736818313573197531378070122258446846208696332202140441601055183195303569747035132295102566133393090514109468599210157777972423137199252708312341156832737997619441957665736148319038440282486060886586224131974679312528053652031230440066166198113855072834035367567388441662394921517
c = 7060838742565811829053558838657804279560845154018091084158194272242803343929257245220709122923033772911542382343773476464462744720309804214665483545776864536554160598105614284148492704321209780195710704395654076907393829026429576058565918764797151566768444714762765178980092544794628672937881382544636805227077720169176946129920142293086900071813356620614543192022828873063643117868270870962617888384354361974190741650616048081060091900625145189833527870538922263654770794491259583457490475874562534779132633901804342550348074225239826562480855270209799871618945586788242205776542517623475113537574232969491066289349
ph = 914008410449727213564879221428424249291351166169082040257173225209300987827116859791069006794049057028194309080727806930559540622366140212043574
q1l = 233711553660002890828408402929574055694919789676036615130193612611783600781851865414087175789069599573385415793271613481055557735270487304894489126945877209821010875514064660591650207399293638328583774864637538897214896592130226433845320032466980448406433179399820207629371214346685408858
e = 0x10001
qh = (n//(ph<<545))>>545


PR1.<x, y> = PolynomialRing(Zmod(n), 2)
PR2.<a, b> = PolynomialRing(Zmod(n), 2)

pa = a + ph*2**545

qx = y + qh*2**545

qa = a +qh*2**545

q1y = y*(2**955) + q1l
q1b = b*(2**955) + q1l

g = qx**2*q1y - qx
rs1 = coppersmith_multivariate_heuristic(g, [2**545, 2**69], beta = 1)

print(f" [+] {rs1 = }")

ql = rs1[0][0]
q = int(ql+qh*2**545)
p = n//q
d = inverse(e, (p-1)*(q-1))
print(long_to_bytes(pow(c, d, n)))