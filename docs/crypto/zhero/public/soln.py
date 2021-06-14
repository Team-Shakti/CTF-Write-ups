from Crypto.Util.number import *
from Crypto.PublicKey import RSA 

ct_a=1991374644522844726604723395302447678829362766488998002689642863876589167224123634868869407586265887639572846618361378190717796457675877867002990630200549839187693737176043693114429036857443618075597595356236777647214186597416429862630588853297534066191784060030827904725960955181749644590885127762513958644117342351741609981560458367036971039921421548984093411630930209440031060634872093143755813835906517674672118355461511837533783279547447855290393938723966500874359457216314821548439555245649159786182924722770460929014017979622168454175758261065999271764594369618940918533185330319317089809708951104047147411596
ct_b=11560415492145861207516424108577715664730529386805857287246533744961821151018194362544284902991666685182413092786353089517543091603274250128250910669110530206320138191614471688310529571895441809729559056935543845898702106837033971935287923495445981173899073238286288875669342754013550227359718814123485311705960547980778357375585882146296937739196745327987012437076826111202650212821723168353665944362122152786549834258495316372518691633486765982945106049194892430437710982481105051765183397588927444843790029563399175420351710322220501327577415113508236805750358567711052779340011355629159610689505604941700815518380
d_a=12007894588345817095001901772235818535532128075248502006167506715501613386280619988757005912270381074208611126718938214462213079931302423653355153363846803336576965899104058007549509604040316897464770127372797630135493394807353800174267249408200186888724103432412296802728616667116382243738519746110159825921676647202689661952040602841752466515868580858475210918168761862255041985423595605698941150797550252491451770611246462256935118062094973933183288422900540413805923476283359196218128607678993284504582128505198491110084905108072190837781925478455984417366202863689318005069821086805269764308054632708127147397685
d_b=15309121030008789112453654624398278092026139678301334759817236349957760197277968332173160272007689043235997494440248487531238644015060915059836861728115118555482791561589562225055947155368216166612774271639118879220806859714069050410034235487298164832205885978355955618431606156727831992132535894020870312453902803351757466444078059503362362343138846985263572980446344678973847354860739168547872456538618897496981232096868408852088578700314051200160980186449222946973789039336701174360592471866811887750298968395798446811465432587371913161943176018766518394820191044593922558127924048562996714970537749736086175516533
e=65537

#Find phin_a,phin_b from d*e = 1mod phin
phin_a= 786961387636419814955139636447018839363169077667561075978199887613829236496672992203167896472463964460409747411779053761210058619457766938969936686006427950269244614129582649640772210919990248509148639837631038286189830615489546002020952724465215648126311566650004695560425350512806343107891368600821544511428922427722672375350884988439931398050479183721889897944026146166608686598706185210691506199819050897532274690549259396932756832435518306659033173371632717099598806865182511642547494561458182886576798955845193511881634426067727170935714050081569850760928837077606834098260864565956964543456976463792528859002081844
phin_b= 1003313864943686012062875163119189951317117116096834576154142218667181730049006210585632404746567916826557567793130565127334787012815047190276528407075480524770675710571895139543491608721366782911301387440412933987494019165080943356722413691131059828608277149363514263365152172693471925268390004886445777667291428023264129078345543785671859140882290614873218782419512091225909034095508262889121917184171466685259659007932464910939329182282481973504950158479322724275821212271009384864070148828735250687491343491755442808683010055478593072894269926741901316041330860489551902692029758370673115709024132504453879684827023220
p = 177279130816191665059944783286411855023035031289227941571673915784074353287733189099688126318264113305321082059619767094038966996649561164342515779196140056547333435193040798074799909334916510316728847254833619137382153503950749154356946058670079132324988450725735937306884337410304401871741381990982764516163
pt_a = long_to_bytes(pow(ct_a,d_a,p))
pt_b = long_to_bytes(pow(ct_b,d_b,p))

print(pt_a)
print(pt_b)


#b'Hey Dave its Alice here.My flag is zh3r0{GCD_c0m3s_'
#b'Hey Dave its Bob here.My flag is 70_R3sCue_3742986}'