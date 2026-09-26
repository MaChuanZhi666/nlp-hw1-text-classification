# T1 全部错分样本与局部贡献

row_id 是原始 CSV 中从 0 开始的数据记录编号。贡献为预测类减真实类的线性分数差中的词项，不含截距；confidence 未校准。

## binary：16 个错误

### row_id=6999：business → politics

confidence=0.795175

原文：

weeks of frantic technical work appear to have made the government's health care website easier for consumers to use. but that does not mean everyone who signs up for insurance can enroll in a health plan .the problem is that the systems that are supposed to deliver consumer information to insurers still have not been fixed. and with coverage for many people scheduled to begin in just 30 days, insurers are worried the repairs may not be completed in time."until the enrollment process is working from end to end, many consumers will not be able to enroll in coverage," said karen m. ignagni, president of america's health insurance plans, a trade group .the issues are vexing and complex. some insurers say they have been deluged with phone calls from people who believe they have signed up for a particular health plan, only to find that the company has no record of the enrollment. others say information they received about new enrollees was inaccurate or incomplete, so they had to track down additional data — a laborious task that will not be feasible if data is missing for tens of thousands of consumers .in still other cases, insurers said, they have not been told how much of a customer's premium will be subsidized by the government, so they do not know how much to charge the policyholder.in trying to fix healthcare. gov, president obama has given top priority to the needs of consumers, assuming that arrangements with insurers can be worked out later. the white house announced on sunday that it had met its goal for improving healthcare. gov so the website "will work smoothly for the vast majority of users ."in effect, the administration gave itself a passing grade. because of hundreds of software fixes and hardware upgrades in the last month, it said, the website — the main channel for people to buy insurance under the 2010 health care law — is now working more than 90 percent of the time, up from 40 percent during some weeks in october.jeffrey d. zients, the presidential adviser leading the repair effort, said he had shaken up management of the website so the team was now "working with the velocity and discipline of a high-performing private sector company ."mr. zients said,000 people could use the website at the same time and that the error rate, reflecting the failure of web pages to load properly, was consistently less than 1 percent, down from 6 percent before the overhaul.pages on the site generally load faster, in less than a second, compared with an average of eight seconds in late october, mr. zients said.whether mr. obama can fix his job approval ratings as well as the website is unclear. public opinion polls suggest he may have done more political damage to himself in the last two months than republican attacks on the health care law did in three years.people who have tried to use the website in the last few days report a mixed experience, with some definitely noticing improvements."every week, it's been getting better," said lynne m. thorp, who leads a team of counselors, or navigators, in southwestern florida . "it's getting faster, and nobody's getting kicked out."but neither mr. zients nor the department of health and human services indicated how many people were completing all the steps required to enroll in a health plan through the federal site, which serves residents of 36 states .and unless enrollments are completed correctly, coverage may be in doubt.for insurers the process is maddeningly inconsistent. some people clearly are being enrolled. but insurers say they are still getting duplicate files and, more worrisome, sometimes not receiving information on every enrollment taking place ." health plans can't process enrollments they don't receive," said robert zirkelbach, a spokesman for america's health insurance plans .despite talk from time to time of finding some sort of workaround, experts say insurers have little choice but to wait for the government to fix these problems. the insurers are in "an unenviable position," said brett graham, a managing director at leavitt partners, which has been advising states and others on the exchanges . "although they don't have the responsibility or the capability to fix the system, they're reliant on it."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|republican|1|+1.232655|
|law|1|+1.065501|
|obama|1|+1.032788|
|he|1|+0.917328|
|gov|1|+0.838101|
|house|1|+0.791979|
|his|1|+0.764993|
|political|1|+0.669441|
|mr|1|+0.540515|
|coverage|1|+0.536982|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|company|1|-2.064702|
|trade|1|-0.806061|
|are|1|-0.615550|
|consumers|1|-0.602140|
|rate|1|-0.566856|
|much|1|-0.550219|
|its|1|-0.529711|
|consumer|1|-0.496309|
|for|1|-0.486115|
|additional|1|-0.437463|

### row_id=9312：politics → sports

confidence=0.495159

原文：

from the day in 1983 when he graduated cum laude from baylor university, tim smith fit the profile of a star alumnus. he went on to earn an m.b.a. at harvard and to lead an information technology company with 300 employees. the business school at baylor invited mr. smith to speak to classes about "entrepreneurial finance," and he was named twice to its advisory board .then, as the fall semester began in, word reached the business school's dean that mr. smith was gay and living with his partner. mr. smith was ousted from the advisory board because his sexual orientation was deemed incompatible with baylor's baptist affiliation and theology."you might as well tell rosa parks that she's welcome in the back of the bus," mr. smith, now, wrote at the time in an e-mail to the dean. "any kind of limitation which puts people 'in their place' on some basis other than merit is not just bad business, it is wrong."a generation later, as baylor holds its commencement ceremonies this weekend in waco, tex., the most famous member of the senior class will be an openly lesbian basketball star, brittney griner . the center on baylor's national championship women's basketball team in, twice the winner of the naismith trophy as the nation's top female player, first pick in the recent w.n.b.a. draft, ms. griner came out last month in a sports illustrated interview, followed by an essay in the new york times .by dint of her celebrity status, to say nothing of her marketplace value to the baylor brand, ms. griner has instantly altered the relationship between baylor and its gay students, one that has been awkward at best and contentious at worst. far from condemning her as a sinner, baylor offered ms. griner "our admiration, appreciation and support," as the university's director of media communications, lori w. fogleman, wrote in an e-mail this week.plenty of caveats should be attached to this tolerance offensive. baylor continues to omit sexual orientation from its nondiscrimination policy. the university's official statement on sexual misconduct lists "homosexual acts" — as well as sexual harassment and adultery, among other behaviors — as "misuses of god's gifts."even so, if it is too soon to know with certainty whether baylor's public acceptance of ms. griner's sexuality will extend to the john and jane queer of its rank-and-file student body, a more expansive kind of change seems possible thanks to what one might call the griner effect."the fact that she felt free enough to do that says something about the environment becoming more accepting than in the past," mr. smith said in a telephone interview last week. "my impression is that the student body there is really pretty accepting, as students are at most campuses these days. the bigger issue is probably with donors and alumni of another generation."erica heath, 20, a junior at baylor, has never watched the women's basketball team play, and has spotted its star player only once, eating in the same student cafeteria.yet ms. heath typifies the kind of garden-variety l.g.b.t. student at baylor who may benefit from the opening ms. griner has created."the fact that this celebrity comes out means that faculty and staff have to recognize that there are l.g.b.t. students on their campus," ms. heath said. "it can make teachers more aware of who they're speaking to. it's very easy to think you're in an all-straight, all- christian community at baylor . but you aren't."baylor's history on gay issues has been a decidedly rocky one, with mr. smith's ouster and the policy language only part of the saga.in, a law firm retained by the university issued a cease-and-desist order against a group of gay and lesbian alumni using the logo " baylor bear pride." also in the early 2000s, university employees washed off a sidewalk chalk message from a student l.g.b.t. support group called "baylorfreedom." (ms. fogleman said that action was consistent with overall university policy, not directed at gay groups .)more recently, baylor has refused formal recognition to sexual identity forum, a group of l.g.b.t. and "questioning" students that includes ms. heath. before becoming baylor's president in, kenneth w. starr helped argue the california supreme court case defending proposition, the state's ban on same-sex marriage .even before ms. griner came out, though, signs of change were appearing. the university does allow sexual identity forum to meet openly in the student center. an economics professor, aaron hedlund, wrote an op-ed column in the student newspaper contending that one can disapprove of gay marriage on religious grounds while supporting it as a civil right.emerson collins, 33, who graduated in 2002 as part of baylor's elite university scholars program, came out only after leaving waco. he is collaborating with another baylor alumnus, del shores, on an indie film, "southern baptist sissies," about four boys growing up gay in fundamentalist christian communities. so mr. collins has watched the brittney griner affair with acute interest."someone always has to be first," he said. "and when there's a great shining beacon who can be respected for who they are in addition to being in the l.g.b.t. community, that can make a big difference. baylor is going to continue to tout her success in her skill set. there's so much commercial benefit to baylor and its national profile . and you can't separate that from who she is. while it's a one-off, that's the way every important journey begins."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|team|1|+1.365921|
|player|1|+1.304940|
|sports|1|+1.163213|
|the|1|+1.013713|
|play|1|+0.827861|
|in|1|+0.749026|
|championship|1|+0.654823|
|and|1|+0.633930|
|to|1|+0.619425|
|against|1|+0.581105|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|mr|1|-3.028564|
|ms|1|-1.074543|
|state|1|-0.901568|
|law|1|-0.891334|
|people|1|-0.712464|
|california|1|-0.599480|
|supreme|1|-0.543764|
|john|1|-0.534996|
|about|1|-0.521507|
|support|1|-0.521100|

### row_id=6688：business → sports

confidence=0.549786

原文：

i'm a 24-year-old entrepreneur in mobile technologies. i haven't been flying for business all that long, but it's really important to my company's growth . i almost always leave home without doing much in terms of checking on my flight, having ground transportation or a hotel reserved. that may sound irresponsible, but i've found that mobile apps can do almost everything for me when i'm on the road.i first learned about how an app could really be helpful when i and several colleagues were working around the clock on a presentation for a client in los angeles . the presentation was planned for a wednesday. but monday afternoon, the client called and asked me to meet him in los angeles early tuesday morning . i needed to leave new york that afternoon if i had any shot of making the new meeting time.i left the office with only my laptop and my phone, and on the way to my apartment, i booked a ticket with an app and checked into my flight. i threw a few things into a bag, and then ran outside, hoping to catch a cab. but it was 4 p.m. and a shift change. there were no cabs in sight.i pulled up another app, booked a car, and was soon on my way to la guardia airport . i closed the deal the next day, and ever since i've been addicted to apps . i only wish there was an app to help me skip security .being a young guy, i really don't know that much about how to deal with children. on a recent flight from kennedy airport to beijing, i found myself sitting next to an 8-year-old boy. i'm not sure parents of six kids would know how to deal with him.just before taking off, the boy's father stood up from a few aisles away and mentioned casually to me, "just warning you. he's a talker."  i thought i could handle an 8-year-old. i was wrong. i had a 13- hour flight sitting next to probably the most curious juvenile on the planet.for the first few hours of the flight, the boy was playing loud video games . when those got old, he created the hilarious game of turning my reading light on and off to get a reaction from me. i tried being polite. i tried a semi-angry look. the little boy thought i was absolutely hysterical.his parents were oblivious to what was going on, chatting quietly before closing their eyes for a nap. lucky them. this boy was nonstop.during mealtime, he and i were served our appetizers, but for some reason the boy didn't receive his entree.   when i realized he had been skipped, i told the flight attendant he needed more food. at this point, i was midway through my dessert, and because of the language barrier, the flight attendant thought i said the boy needed another dessert. he got one. i was probably his hero.just as the boy had finished his first dessert and was moving onto his second, his mother woke up and came over to check on her child. she saw his empty dessert plate and then saw him diving into dessert no. 2. she started yelling at him in mandarin. though i speak a bit of mandarin, i stayed out of the conversation. i didn't want to get yelled at.she gave up and let her boy finish the second dessert. so now i'm stuck for the next five hours sitting next to an already talkative 8-year-old who is on a sugar high. good times. there wasn't an app invented that could save me.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|game|1|+1.414923|
|he|1|+1.032345|
|his|1|+0.979724|
|games|1|+0.963629|
|the|1|+0.793649|
|playing|1|+0.757731|
|in|1|+0.743707|
|to|1|+0.623807|
|him|1|+0.623162|
|times|1|+0.463396|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|company|1|-1.590619|
|flight|1|-0.835910|
|about|1|-0.765519|
|or|1|-0.732768|
|started|1|-0.670971|
|an|1|-0.535767|
|food|1|-0.500199|
|much|1|-0.498330|
|some|1|-0.497186|
|new|1|-0.485712|

### row_id=4113：business → politics

confidence=0.998224

原文：

a group of state insurance commissioners emerged from a meeting with president obama and other federal officials on wednesday saying that state regulators would continue to decide on their own whether to go along with his recent proposal to let consumers keep older insurance plans for an extra year, even if the plans did not comply with regulations under the new health care law.in a conference call with reporters and in a statement issued after the meeting, they said they told the president they would not reach any consensus on what states should do. they said they warned the president that his proposal would amount to "different rules for different policies and might result in higher premiums for consumers without addressing underlying concern of gaps in coverage ."jim donelon, president of the national association of insurance commissioners and the louisiana insurance commissioner, said in a statement that members of his organization, which represents state insurance commissioners, "have been working to ensure that plans are compliant with the new rules."he added, "these proposed changes are creating a level of uncertainty that we must work together to alleviate." white house officials acknowledged that each state had to make the decision that was best for its consumers ." states have different populations with unique needs, and it is up to the insurance commissioner and health insurance companies to decide which insurance products can be offered to existing customers next year," the administration said in a statement.the meeting, which lasted 50 minutes, had a conciliatory tone, the regulators said, even as they declined to recommend a course of action to their counterparts across the country. the regulators said policy recommendations were not part of their mission."we share the president's goal of affordable coverage for consumers, and we will work with the insurance companies in our states to implement changes that make sense while following our mandate of consumer protection," mr. donelon said.mr. donelon attended the meeting with former senator ben nelson of nebraska, who is chief executive of the organization; the connecticut insurance commissioner, thomas b. leonardi; and the north carolina insurance commissioner, wayne goodwin. kathleen sebelius, the secretary of health and human services and the highest-ranking official overseeing the health care law, was also there.mr. obama announced his proposal days earlier, intending to make good on his often-repeated pledge that consumers who liked their insurance plans could keep them. despite his pledge, insurers have sent out cancellation notices to millions of people in recent weeks . the cancellations, which insurers attributed largely to the new health care requirements, had created anxiety among holders of health policies and was being used by political opponents to attack another aspect of the health care law .although the president urged insurers to renew older policies for another year, the decision is ultimately up to insurance companies, which write the policies, and state insurance regulators, who typically have final say over whether the old policies can be sold and what insurers can charge for them.some states, like florida, have said they will allow consumers to renew old policies, but others, including washington and indiana, have said they will not adopt mr. obama's proposal. new york has also said it will not comply with the president's request. california is to announce its decision on thursday.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|1|+1.463487|
|washington|1|+1.085620|
|law|1|+1.065501|
|obama|1|+1.032788|
|officials|1|+0.936693|
|he|1|+0.917328|
|house|1|+0.791979|
|his|1|+0.764993|
|senator|1|+0.703982|
|political|1|+0.669441|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|companies|1|-1.057476|
|are|1|-0.615550|
|consumers|1|-0.602140|
|chief|1|-0.563369|
|its|1|-0.529711|
|products|1|-0.528103|
|amount|1|-0.511441|
|consumer|1|-0.496309|
|for|1|-0.486115|
|share|1|-0.481819|

### row_id=5275：business → politics

confidence=0.514874

原文：

home buyers purchasing energy-efficient properties could qualify for larger mortgages than their incomes would normally allow under a senate bill reintroduced thursday with broad real estate industry support.the measure would allow lenders to include projected energy savings from efficiency upgrades when measuring the borrower's income against expenses and the value of the home against the debt . in addition to giving borrowers larger loans in new purchases and refinancings, it could also lower their interest rates. senator johnny isakson, a republican from georgia who worked in the real estate industry for 33 years and introduced the bill with senator michael bennet, a democrat from colorado, said that consumers should get credit for energy-saving construction materials, which are often "out of sight and out of mind and are not valued." decreasing the amount of energy a home uses, he said in an interview, increases "the amount of dollars in the pockets of the homeowners."the government already promotes so-called energy-efficient mortgages under a department of housing and urban development program. but the proposed legislation would require lenders to take the projected energy savings into account when presented with a qualified energy report. the senators originally introduced the bill in, and although it attracted support from groups across a broad political spectrum — including the united states chamber of commerce and the center for american progress — it failed to gain approval. the sponsors have broadened its appeal within the real estate industry, chiefly by eliminating provisions that could have penalized older, less efficient homes or those lacking a report based on estimated energy consumption .how the bill will fare this time around is unclear. its proponents in the senate say they are hopeful it could pass, possibly as part of a comprehensive energy bill introduced by senator jeanne shaheen, a democrat from new hampshire, and senator rob portman, a republican from ohio . the proponents say the changes could curtail energy use, reduce greenhouse gas emissions and increase the market for conservation upgrades.the legislation would apply to loans guaranteed by the federal agencies that collectively back roughly 90 percent of new mortgages .in the absence of a home energy report, which would come from an approved third- party inspector, the home's energy use would not become a factor. but lenders would provide applicants with information about the benefits of investing in energy-saving upgrades and counsel them on how they could go about doing so."really we're just talking about disclosure here," sean babington, legislative counsel on energy and natural resources for senator bennet, said in an interview. "for years you've had to disclose if there are termites in your house or if you have radon gas in your basement. you bring an inspector out to make sure the foundation's not cracked. here we have something that probably over the life of the home costs the homeowner orders of magnitude more than all those problems, and we totally ignore it."according to senator bennet's office, a household's average energy costs can run to more than,000 over the life of a 30-year loan, more than the real estate taxes and insurance payments that are already taken into account during the underwriting process. investments in insulated hollow-core doors, double-pane windows and insulated floor-joist systems above crawl spaces can reduce the average home's bill by at least 30 percent, a value that does not always translate into a higher purchase price .jonathan j. miller, the president of miller samuel, an appraisal firm, said the consensus in the real estate market was that "people want green, but to date they haven't been willing to pay for it to the extent of what it costs ."if passed, proponents say, the proposal could help close that gap, in addition to promoting energy conservation and construction jobs, generating.1 billion a year in savings for consumers by.loan applicants could expect to gain about 5 percent more borrowing power on average, said cliff majersik, executive director of the institute for market transformation, a nonprofit group that promotes energy efficiency in buildings and helped shape the proposal."many people buy what they can qualify for and no more and no less," he said. "there are $2 trillion in mortgage loans that happen every year, and the fact that you have this big blind spot is an enormous impediment to energy efficiency ."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|republican|1|+1.232655|
|he|1|+0.917328|
|house|1|+0.791979|
|senator|1|+0.703982|
|political|1|+0.669441|
|senate|1|+0.584547|
|groups|1|+0.575828|
|support|1|+0.570672|
|said|1|+0.508946|
|here|1|+0.501777|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|market|1|-1.121527|
|industry|1|-0.792309|
|are|1|-0.615550|
|consumers|1|-0.602140|
|billion|1|-0.561455|
|credit|1|-0.555656|
|its|1|-0.529711|
|big|1|-0.520466|
|mortgage|1|-0.511447|
|amount|1|-0.511441|

### row_id=6330：politics → business

confidence=0.835543

原文：

anticorruption activists have urged president obama to back a plan to publicly register the owners of shell companies in the united states and around the world, a move they say is essential to thwart corrupt government officials, tax evaders and money launderers who rely on an opaque financial system.the plan, backed by prime minister david cameron of britain this year, was outlined in letters sent to mr. obama last week by two groups of current and former prosecutors and activists . the issue is set to be raised again at the group of 8 summit meeting of industrialized countries this month."corrupt politicians, tax evaders, and organized criminals all use complex webs of shell companies to hide and launder stolen money," said 19 prosecutors and activists in one of the letters. the group calls for " governments to require existing company registers to collect information on the ultimate owners of all companies " and for that information to be publicly available. france and italy are also thought to back the proposal, said stefanie ostfeld, a senior policy adviser for the anticorruption research group global witness, but while the united states has expressed an interest in such information being made available to law enforcement officials, it has appeared reluctant to make it public. opponents of the measure say it would be expensive, increase bureaucracy and discourage business ."these anonymous shell companies are used by everybody who steals money," said jack a. blum, a lawyer and the chairman of tax justice network usa, who was among those who signed the letters. tens of thousands of shell corporations have been set up within the united states, he said, primarily in four states — delaware, montana, nevada and wyoming — that have loose regulations."we know that the bad guys are selling the u.s. as a place to set up companies," mr. blum said, citing its "aura of legitimacy."while activists say the issue is pressing because of the need to ensure that poorer nations with natural resources are not exploited by unscrupulous officials, it is not a new problem. the financial crimes enforcement network, a bureau of the treasury department, estimated in 2005 that as much as $18 billion in suspicious transactions were made using international wire transfers that used shell companies in the united states . senator carl levin, a michigan democrat, has introduced legislation that would require states to collect information on the "beneficial ownership" of companies incorporated within their borders. it has failed to pass three times since. on one of those occasions, it was co-sponsored by mr. obama, at the time a senator . the white house did not immediately return a call and an e-mail seeking comment on the letters or on mr. obama's position.in britain, mr. cameron's championing of the issue was prompted in part by a series of revelations in recent months that celebrities and other public figures were avoiding taxes using elaborate loopholes.and as a wave of protests and revolutions swept the arab world in, it became clear that the region's dictators had safeguarded their plundered wealth through intricate accounting practices.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|company|1|+2.064702|
|companies|1|+1.057476|
|countries|1|+0.747366|
|are|1|+0.615550|
|financial|1|+0.609342|
|billion|1|+0.561455|
|much|1|+0.550219|
|its|1|+0.529711|
|treasury|1|+0.507534|
|chairman|1|+0.505214|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|law|1|-1.065501|
|obama|1|-1.032788|
|officials|1|-0.936693|
|he|1|-0.917328|
|house|1|-0.791979|
|senator|1|-0.703982|
|groups|1|-0.575828|
|mr|1|-0.540515|
|said|1|-0.508946|
|justice|1|-0.506016|

### row_id=7493：politics → business

confidence=0.656043

原文：

washington — the short-term plan to reduce greenhouse gas emissions that president obama outlined this week is achievable with some new programs and better management of existing ones, the new energy secretary, ernest j. moniz, said in an interview on thursday. but he said reaching a longer-term goal would require bigger reductions as well as action from congress .when mr. obama first ran for president, he pledged to reduce greenhouse gas emissions in the united states 80 percent by, compared with 1990 levels.mr. obama's interim goal, for, is a 17 percent reduction in global warming gas emissions compared with. the 2020 goal is already half achieved, dr. moniz said, and achieving the rest will require faster fulfillment of new appliance efficiency standards, among other steps. many of those standards are stuck in a bottleneck at the office of management and budget, which evaluates the costs and benefits of proposed regulations ."i think the president's commitment will provide the spur to o.m.b. and the energy department to move smartly on these," dr. moniz said.other steps include government loan guarantees for fossil fuel projects that will cut pollution, which the energy department will administer but has yet to describe in detail." fossil fuels are not going away any time soon," dr. moniz said. he said it was essential to build power plants that would capture and bury their carbon dioxide emissions and that after that technology was commercialized for coal it would have to be used on natural gas as well. carbon emissions from power plants that use natural gas are about half of those from coal, but they are still not nearly small enough to meet long-term climate goals, he said.another step, he said, is the completion of new civilian nuclear power reactors at a price and on a schedule close to what has been budgeted. the department is still negotiating a loan guarantee for one of those projects, vogtle 3 and, near waynesboro, ga. he said that the four new reactors under construction — the other two are in south carolina — were only slightly larger, in capacity, than the four reactors whose retirements have been announced this year. in the long term, he said, it was essential that the plants under construction become templates for building more.by midcentury, when the president's goal is an 80 percent reduction in emissions compared with, "you have to replace essentially all the nuclear capacity, and build more," he said.production of a new kind of factory -built "small modular reactors " would also be needed, but those would not be deployed by, he said.one of the big steps the president described this week was setting standards for carbon dioxide emissions from power plants . the energy department might play a role in helping improve power plant efficiency, but the standards would be set by the environmental protection agency .to reach the 80 percent goal, set forth by mr. obama when he first ran for president, would require cutting emissions every year by about 20 percent more than what the president proposed this week, said daniel m. kammen, director of the renewable and appropriate energy laboratory at the university of california, berkeley. mr. kammen also said the 17 percent goal is "not as deep as i would like initially, but it's critical to do this step."dr. moniz said that the interim goal was compatible with the long-term goal, but reaching the 2050 goal "would require a lot more to happen."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|are|1|+0.615550|
|production|1|+0.533412|
|big|1|+0.520466|
|global|1|+0.488287|
|for|1|+0.486115|
|initially|1|+0.441847|
|an|1|+0.431396|
|energy|1|+0.422806|
|plant|1|+0.418896|
|levels|1|+0.406475|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|washington|1|-1.085620|
|obama|1|-1.032788|
|he|1|-0.917328|
|programs|1|-0.735020|
|secretary|1|-0.608660|
|mr|1|-0.540515|
|south|1|-0.519382|
|said|1|-0.508946|
|california|1|-0.484140|
|congress|1|-0.452432|

### row_id=2778：business → sports

confidence=0.673538

原文：

washington — hyatt hotels has reached a tentative contract with the union representing thousands of its employees, ending a four-year dispute that led to dozens of protests and a global boycott against the chain, based in chicago .the agreement between hyatt and the union, unite here, was announced on monday and will go into effect once union contracts are approved by workers in chicago, honolulu, los angeles and san francisco . the contracts would provide retroactive wage increases and keep employees' current health care and pension benefits through.over the last two years, the union held a number of one-day strikes in major cities to protest wages and working conditions .unite here said the accord would end its global boycott of hyatt, which had support from other unions, workers' rights groups and civil rights organizations.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|the|1|+0.793649|
|in|1|+0.743707|
|to|1|+0.623807|
|contract|1|+0.464829|
|year|1|+0.457395|
|will|1|+0.431426|
|major|1|+0.367987|
|against|1|+0.338954|
|of|1|+0.328637|
|was|1|+0.309799|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|its|1|-0.735923|
|are|1|-0.708098|
|which|1|-0.699294|
|union|1|-0.453823|
|global|1|-0.439871|
|that|1|-0.403238|
|workers|1|-0.334380|
|unions|1|-0.299743|
|other|1|-0.295910|
|would|1|-0.233675|

### row_id=4565：business → politics

confidence=0.959737

原文：

this spring, the missouri chamber of commerce urged the state legislature to accept the federal government's plan to expand medicaid for the poor and disabled.the business lobbying group had not suddenly gone rogue. here is how daniel p. mehan, its president, summarized his feelings about president obama's health care law : "we don't like it."but the chamber was cognizant of the plea of its members directly affected by the issue: dozens of missouri hospitals stood to lose.2 billion over six years in federal support for uncompensated care if the state refused to increase the income ceiling for medicaid eligibility.pragmatism suggested accepting the expansion. washington would pay the extra cost entirely for three years and pick up 90 percent of the bill thereafter.and it would expand health coverage in the state's poor, predominantly white rural counties, which voted consistently to put republican lawmakers into office.missouri's republican -controlled legislature — heavy with tea party stalwarts — rejected medicaid's expansion in the state anyway.after their vote, a frustrated editorial in the missourian, a faithfully conservative newspaper in washington, mo., asked of the state's elected republicans : "who do they represent?"today, the same forces that blocked the expansion of medicaid in missouri are going all out in washington in a bid to undo all of the affordable care act . bowing to the vehemence of its tea party faction, the house g.o.p. forced a government shutdown when senate democrats refused to delay or defund the president's health overhaul. house republicans are threatening even further damage if they don't get their way, possibly unleashing financial chaos if they manage to force the united states into its first default ever on the government's debt .republicans' efforts raise the same perplexing question posed by the missourian: what drives tea party republicans and their financial backers ? what calculation persuades them that repealing the health care law is worth the risk ? indeed, whose interests do they represent?nearly 6 in 10 americans disapprove of trying to stop the law by cutting its financing . even among those who don't like the law, less than half want their representatives in congress to try to make it fail.it is tempting to discard the tea party activists driving the republican party as crazy — as some commentators have — motivated by fear and willing to believe that default won't cause much harm and might even act as a purgative to free the economy of a bloated government ."they listen to nobody but themselves," the harvard political scientist theda skocpol told me. "they are convinced of their rectitude and convinced that they alone are qualified to save america from the dire threat of obama and his polices. they have worked themselves into a dangerous place."their relationship with reality can take peculiar turns. reflexive opponents of " government," they can exhibit little sense of what the government actually does.and yet the argument that half the republican party has simply lost its mind has to be an unsatisfactory answer, especially considering the sophistication of some of the deep-pocketed backers of the tea party insurgency .there is a plausible alternative to irrationality. flawed though it may turn out to be, obamacare, as the affordable care act is popularly known, could fundamentally change the relationship between working americans and their government . this could pose an existential threat to the small- government credo that has defined the g.o.p. for four decades.the law is imperfect. it has dozens of complicated, interlocking parts. half of americans say they don't understand how it will affect them and their family. still, the law has many provisions that are likely to improve life for millions of americans, including a big portion of what we know as the working middle class .almost two-thirds of uninsured americans have a full-time job, according to the kaiser family foundation . a further 16 percent are employed part time.the department of health and human services recently estimated that nearly six in 10 uninsured americans could qualify for health coverage in the insurance market for less than $100 per person per month.according to an analysis by the urban institute, 28 million americans would gain health insurance under obamacare . of these, eight million earn more than twice the poverty level of,100 for a family of four. a majority of those would get a subsidy to buy a plan.as it turns out, the core tea party demographic — working white men between the ages of 45 and 64 — would do fairly well under the law.take missouri . it has about,000 uninsured. almost half of them would have been eligible for expanded medicaid benefits, had the legislature not rejected them. many of the rest — including families of four making up to,000 — will be eligible to get subsidized health insurance .in st . louis, for instance, a family of four making,000 a year will be able to buy a middle-of-the-road "silver" health plan for $282 a month and a bottom-end "bronze" plan for. even medicare recipients will get a benefit worth a few hundred dollars a year.in, when president bill clinton took an earlier stab at a health care overhaul, the conservative thinker william kristol published a manifesto about why republicans had to stop it." passage of the clinton health plan in any form would be disastrous," mr. kristol wrote, italicizing for emphasis. "it would guarantee an unprecedented federal intrusion into the american economy . its success would signal the rebirth of centralized welfare-state policy at the moment that such policy is being perceived as a failure in other areas."two decades after mr. clinton's ultimately failed attempt, obamacare poses the same sort of threat.even americans who say they dislike the law actually like many of its components. nearly three-quarters approve of giving financial help to poor and moderate- income americans to buy health insurance . two-thirds approve of barring insurance companies from denying coverage because of somebody's medical history . three-quarters favor letting children stay on their parents' insurance until they are.until now, social welfare programs in the united states have exhibited a "big hole," professor skocpol said, consisting of nonpoor working-age americans and their children. obamacare closes a big chunk of it."the main beneficiaries tend to have lower wages, employed in smaller businesses that are not providing health insurance," she said. "they are not elderly. they are also not the poorest."and they might be grateful to democrats for the benefit.to conservative republicans, losing a large slice of the middle class to the ranks of the democratic party could justify extreme measures.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|1|+1.463487|
|republican|1|+1.232655|
|washington|1|+1.085620|
|law|1|+1.065501|
|obama|1|+1.032788|
|republicans|1|+0.958460|
|house|1|+0.791979|
|his|1|+0.764993|
|programs|1|+0.735020|
|political|1|+0.669441|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|market|1|-1.121527|
|companies|1|-1.057476|
|professor|1|-0.803970|
|measures|1|-0.764577|
|are|1|-0.615550|
|financial|1|-0.609342|
|today|1|-0.604599|
|billion|1|-0.561455|
|much|1|-0.550219|
|its|1|-0.529711|

### row_id=2880：sports → politics

confidence=0.867488

原文：

a report commissioned by the family of joe paterno, a former penn state football coach, said he was unfairly tarnished and implicated in the sexual abuse scandal involving jerry sandusky, a longtime assistant who was convicted last year of sexually assaulting 10 boys.the 238- page report, which was compiled by a team led by richard thornburgh, a former united states attorney general, and released sunday, said an even larger investigation into the sandusky case by louis j. freeh, a former f.b.i. director, was "factually wrong, speculative and fundamentally flawed."according to the thornburgh report, the freeh inquiry, which was ordered by the penn state board of trustees and released in july, falsely accused paterno of helping to cover up sandusky's repeated abuse to shield the university from adverse publicity, and wrongly blamed the " football culture" at penn state for helping foster sandusky's crimes .the freeh inquiry failed to conduct interviews with "most of the key witnesses," the thornburgh report said, including penn state's top executives, its police and the district attorney's office in centre county, where the university is. also, no one testified under oath for the freeh investigation, the thornburgh report said, and witnesses were allowed to speak anonymously.since sandusky was arrested in late, the paterno family has been adamant that paterno, who died jan. 22, 2012, did not cover up sandusky's crimes and that he followed university protocol in 2001 when he reported to his superiors an accusation about sandusky that had been brought to his attention. mike mcqueary, then a graduate assistant, told paterno of an encounter between sandusky and a child in a penn state locker room shower. paterno said he relayed the account to tim curley, the athletic director, and gary schultz, then a university vice president .the university fired paterno after the scandal broke . the n.c.a.a. used the freeh report as the basis for its decision to impose penalties on the university and the football program, including a $60 million fine, a loss of scholarships and a four-year postseason ban.the thornburgh report, which was titled "critique of the freeh report : the rush to injustice regarding joe paterno," repeated many of the claims made by the family. freeh, who had declined to address criticisms of his report, issued a statement sunday."i respect the right of the paterno family to hire private lawyers and former government officials to conduct public media campaigns in an effort to shape the legacy of joe paterno," freeh said. "however, the self-serving report the paterno family has issued today does not change the facts established in the freeh report or alter the conclusions reached in the freeh report ."freeh noted that paterno declined to speak with him even though he spoke with a news reporter and his biographer.instead, freeh cited paterno's testimony under oath before a grand jury and included documents provided by paterno's lawyers in the report. several other university officials did not speak with freeh, including schultz and curley. curley has been on administrative leave. he, schultz and graham b. spanier, the university president fired in the wake of the scandal, all face charges, including perjury, obstruction of justice, endangering the welfare of children and criminal conspiracy."mr. paterno was on notice for at least 13 years that sandusky, one of his longest-serving assistants, and whose office was steps away, was a probable serial pedophile," freeh said. "i stand by our conclusion that four of the most powerful people at penn state failed to protect against a child sexual predator harming children for over a decade."the thornburgh report drew the opposite conclusion about paterno, who spoke to the investigators his family hired. the report said that freeh had "unilaterally anointed himself the judge, jury and executioner by deciding to redefine jerry sandusky's personal crimes as a penn state and joe paterno football scandal."freeh did not properly acknowledge that sandusky was a "masterful manipulator" who deceived an entire penn state community to "obscure the signs of child abuse " and "fooled qualified child welfare professionals and law enforcement, as well as laymen inexperienced and untrained in child sexual victimization, like joe paterno," the thornburgh report said.paterno, the report said, knew little of sandusky's personal life . it added, "the freeh report missed that they disliked each other personally, had very little in common outside work and did not interact much if at all socially."the information that paterno was given about sandusky's abuse in 2001 was "too general and vague for him to disregard decades of contrary experience," the report said. a psychologist hired by the paterno family to examine his life determined that paterno "acted honestly and in good faith throughout the sandusky scandal," starting more than a decade ago when some of the first reports of child abuse were brought to his attention.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|mr|1|+3.028564|
|state|1|+0.901568|
|law|1|+0.891334|
|judge|1|+0.866923|
|county|1|+0.841555|
|officials|1|+0.747722|
|government|1|+0.746108|
|people|1|+0.712464|
|justice|1|+0.670244|
|police|1|+0.649305|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|team|1|-1.365921|
|football|1|-1.243802|
|coach|1|-1.173336|
|the|1|-1.013713|
|in|1|-0.749026|
|sunday|1|-0.697175|
|and|1|-0.633930|
|to|1|-0.619425|
|against|1|-0.581105|
|of|1|-0.537426|

### row_id=10714：business → politics

confidence=0.983900

原文：

as the obama administration's health overhaul sputters in its opening weeks, insurers and advocacy groups are pursuing a new strategy in the quest to get millions of young people to sign up for health insurance : they're appealing to their mothers.in one cheeky campaign, aarp is urging mothers to send e-cards to their children reminding them to sign up. one e- card reads, "as a reward for signing up for health insurance, i'll defriend you on facebook ." another group, organizing for action, is seeking to steer holiday conversations toward health care by encouraging parents to have "the talk" with their adult children . and a colorado group is promoting an ad featuring a hapless young man who calls his mother from the golf course: "yo, mom, do i got insurance ?"recruiting enough young people is a major goal of the obama administration because insurers need healthy customers to offset the cost of caring for those with expensive medical needs.the goal carries even more urgency now that insurers are considering a proposal by president obama to let people, many of them healthy, stay on their existing policies for another year. if fewer of those people buy insurance in the new marketplaces, signing up young people without insurance will be even more crucial. young people also account for a major chunk of the uninsured. about 40 percent of the estimated 41 million uninsured people nationwide who are eligible for coverage are between the ages of 18 and, according to the administration .even as supporters are enlisting mothers in the effort to sign up their adult children, critics have mounted an equally aggressive and well-funded campaign urging young people to "opt out" of coverage . opponents use many of the same marketing tools as the law's supporters, reaching out to young people on social media and through web videos. advocacy groups and insurers are expected to make a major marketing push beginning in early december, when the obama administration has said it expects the malfunctioning federal health care website to be working better. they have their targets set on two major deadlines: dec. 23, when insurance must be purchased for coverage beginning on jan. 1, and march, when the open enrollment period will end.beneath the marketing campaigns' playful language is a deeper truth: when it comes to making major life decisions, many people — especially young adults — still turn to their mothers for help. more broadly, women make about 80 percent of the health care decisions for their families, according to the federal labor department ."it's the cutest phenomenon ever," said lynn quincy, a senior health policy analyst at consumers union, who stumbled on the significance of mothers while conducting a focus group of men and women last year about how well people understood the language in their insurance policies . when asked who they turned to for advice about health care, the overwhelming answer was their mothers. "these people could have husbands, they could have fathers, they may have a nurse who lives next door, but they're all going to their moms," she said.of course, the administration and advocacy groups are also reaching out directly to young people themselves, collaborating with outlets like the comedy website funny or die, initiating social media campaigns, handing out fliers at concerts and sponsoring a video contest aimed at getting young people to sign up."people need to have heard about it a couple of times, and frankly from a couple of different sources," said jon carson, the executive director of organizing for action, the nonprofit group that grew out of president obama's 2012 campaign organization. he said mothers represented just one avenue that they hoped would help persuade a young person to enroll. the recently posted video is part of a campaign, called healthcare for the holidays, that seeks to arm parents with talking points when they see their children at family get-togethers.this approach may resonate especially well with the so-called millennial generation, which came of age in a recession and may still financially depend on their parents, say some experts."millennials love their parents and they count on them for advice," said morley winograd, the co-author of three books on the millennial generation . he noted that this might sound surprising to baby boomers, who famously rebelled against their parents' generation. but millennials "assume that their parents have more worldly experience, and know about things like money and health insurance," he said.mary babich, the mother of two children in their 20s without insurance, said she had been pestering both of them to sign up. "they look at it as just government bureaucracy — as almost akin to filling out their taxes," said ms. babich, who lives in wisconsin . she paused, and added, "the sad thing is, i've always done both of their taxes ."the mother-knows-best strategy isn't entirely new. in, when massachusetts introduced its health care law, officials mailed greeting cards, timed for mother's day, to the parents of young men between the ages of 18 and. market research had shown this group was among the most resistant to buying insurance . "the idea was to trigger a phone call from the parent to the child to say, 'hey, by the way, do you have insurance ?' " said kevin j. counihan, who served as chief marketing officer for massachusetts's health insurance marketplace at the time. "we made the hypothesis that we could best reach the young men through their mothers."the effort, mr. counihan said, was a moderate success: many parents decided to pick up the bill for their sons' health insurance . and more often than not, "we found they bought the most expensive plan because apparently nothing was too good for johnny." mr. counihan is now chief executive of connecticut's state marketplace and said he was still targeting the mothers of young men by focusing on churches and community groups where they are likely to be members. insurers are also taking note of this influence. shaun greene, the chief operating officer at arches health plan, a health care co-op in utah, said he was surprised during a recent televised call-in when he fielded several calls from parents who quickly handed the phone to their children. "at least three of them had their kid by the ear," he said, explaining: "my son or daughter needs insurance . talk to them."a certain level of concern is just part of being a parent, said nicole duritz, who helped develop the aarp campaign. "i'm a mom and i'm constantly worried about my kids, and making sure they're making good decisions," she said. "and health insurance falls into that category."that's certainly true for lynne jackier, of ithaca, n.y., who has been helping her 24-year-old daughter look into buying health insurance on the state marketplace . she also has a 26-year-old son who recently moved to california and is also uninsured."i feel like, as parents, it's our responsibility to get them to look at this now," ms. jackier said.her daughter, rosie simon, works as a nanny in westchester county and said she had been uninsured since graduating from college a few years ago . although ms. simon said that she had heard about the changes coming under the health care law, she added that her mother had been persistent in making sure she signed up. last weekend, during a visit home, the two sat down at the computer and took the initial steps of completing an application on new york's marketplace .without insurance, ms. simon said she often delayed going to the doctor when sick, or leaned on her parents for help. ms. jackier, who is on medicaid and so can't cover her daughter through private insurance, said she had become accustomed to the frustrating conversations. "she'll get sick and i'll say, 'you have go to the doctor,' " ms. jackier said. "and she'll say, 'well, i don't have insurance .' "the family had a scare when ms. simon recently developed a serious kidney infection. her parents paid the bill, which cost a few hundred dollars . it wasn't ideal, ms. simon said, but "i'm still their baby."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|1|+1.463487|
|law|1|+1.065501|
|obama|1|+1.032788|
|officials|1|+0.936693|
|he|1|+0.917328|
|county|1|+0.777282|
|his|1|+0.764993|
|open|1|+0.688413|
|women|1|+0.623708|
|groups|1|+0.575828|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|market|1|-1.121527|
|union|1|-0.743593|
|are|1|-0.615550|
|consumers|1|-0.602140|
|chief|1|-0.563369|
|its|1|-0.529711|
|marketing|1|-0.524257|
|labor|1|-0.510605|
|for|1|-0.486115|
|an|1|-0.431396|

### row_id=3615：sports → politics

confidence=0.536122

原文：

miami — after an 11-day trial, a 23-year-old man charged in the killing of the washington redskins star sean taylor in 2007 was found guilty monday of second-degree murder and armed burglary. prosecutors said the man, eric rivera jr., and four others traveled to palmetto bay, the miami suburb where taylor lived, with the intention of stealing money from him. the burglary went awry, prosecutors said, when the intruders unexpectedly encountered taylor at home and shot him.one of the suspects, venjah hunte, earlier pleaded guilty to second-degree murder and burglary and was sentenced to 29 years, and the remaining three defendants will be tried on lesser charges later. rivera could be given a life term in prison when he is sentenced next month in miami-dade circuit court .the 12-member jury began deliberating last wednesday. the trial attracted considerable attention in south florida, where taylor, a native son who became a standout safety at the university of miami before going to the redskins, was something of a local hero. prosecutors said in opening statements oct. 21 that after breaking into taylor's house with his accomplices, rivera fired two shots, one of which pierced taylor's femoral artery as he confronted the intruders with a machete. taylor's girlfriend and their 18- month-old daughter were unharmed. taylor, 24, died the following day.during the trial, rivera took the stand in his own defense, acknowledging that he had accompanied the other men on the trip to palmetto bay but insisting that he had remained outside taylor's house during the break-in. taylor was shot inside after someone kicked open his bedroom door.but rivera gave a videotaped confession to the police in which he said he had shot taylor. he even drew a sketch of the layout of taylor's home, a prosecutor said, with notations for the burglars' whereabouts during the crime ."this defendant confessed to the murder of sean taylor, that he committed it," assistant state attorney ray araujo told the jury .rivera's lawyer, janese caruthers, said that his client's confession had been coerced by detectives eager to find a culprit in a case that had drawn national attention . prosecutors noted that one of the intruders had previously been to a birthday party at taylor's house and had seen him give,000 to his sister as a present. the robbers, araujo said, thought that taylor was out of town when they went to burglarize his home in the early hours of nov. 26, 2007, and did not know he was at home with an injury.robert parker, a former miami-dade county police director, said the defendants were "certainly not looking to go there and kill anyone," the associated press reported. "they were expecting a residence that was not occupied."the murder weapon was never found, and prosecutors believe that one of the men threw it into the everglades as they drove home to fort myers along alligator alley.taylor was an all-american at the university of miami . he was selected by the redskins in the first round of the n.f.l. draft in.he was named to the pro bowl after his 2006 season, when he led the redskins in tackles .


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|washington|1|+1.267298|
|house|1|+0.966385|
|state|1|+0.901568|
|county|1|+0.841555|
|defense|1|+0.691876|
|police|1|+0.649305|
|trial|1|+0.574410|
|killing|1|+0.564711|
|life|1|+0.534046|
|which|1|+0.516845|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|season|1|-1.161580|
|the|1|-1.013713|
|in|1|-0.749026|
|and|1|-0.633930|
|to|1|-0.619425|
|round|1|-0.572505|
|second|1|-0.571390|
|of|1|-0.537426|
|for|1|-0.488196|
|star|1|-0.446620|

### row_id=9945：business → politics

confidence=0.991281

原文：

in many stores around the country, the workers stocking the shelves and ringing up the gifts are at the very heart of this season's retail lament —many americans are so financially strapped that projections for holiday sales have grown bleaker by the week.and more so than in years past, the focus is on retail workers as more stores open on thanksgiving day, requiring many more to work on the holiday. even if they have the option of staying home, those still stuck at the bottom economic rung long after the recession's end have little choice but to take on extra shifts. food stamps have been cut for some, and many were stung by the payroll tax increase . even their own companies have set up food drives to aid low-paid employees at individual stores or created help lines advising them how to stretch their food dollars and apply for public assistance .chardé nabors, a mother of two who works as a $9-an-hour cashier at sears in the chicago loop, feels left behind by the holiday festivities, partly because she was scheduled to work from:30 p.m. thanksgiving to 6 a.m. friday. "i'm here watching shoppers buy all these items, and i'm working to help these people, and i can't even buy my children the same products," said ms. nabors, whose 3-year-old son wants a spider-man doll she cannot afford.for retail workers nationwide, who earn a median pay of about.60 an hour, or less than,000 a year, holiday shopping sprees are most often enjoyed by customers on the opposite side of the counter.on black friday, workers at walmart and their union allies plan to stage protests at some,500 walmart stores to demand higher pay . moreover, many lawmakers, seeing the squeeze on incomes nationwide, are pushing an idea that they say could give a much-needed boost to retailers' languishing sales: increasing the minimum wage .the idea has been picking up momentum, with several new developments in the last month.the massachusetts state senate approved a measure last week that would increase that state's minimum wage to $11 an hour, far more than the.25-an-hour federal minimum. hoping to reduce low-wage workers' dependence on government aid, a conservative billionaire in california, ronald unz, is backing a referendum to raise his state's minimum wage to $12 — even more than the $10 minimum that gov . jerry brown signed into law in september. and on tuesday, officials in washington state announced that voters in seatac, a seattle suburb, had approved a referendum to establish a $15-an-hour minimum wage for the,500 workers at the international airport there. also this week in maryland, the montgomery and prince george's county councils voted to raise the minimum to.50 an hour by. earlier this month, white house officials said they would back a bill in congress that calls for raising the federal minimum to.10 an hour over two years, although opposition within the republican-controlled house makes passage unlikely anytime soon. major retailers and fast-food companies have opposed an increase, saying it would force them to raise prices and reduce worker numbers.median pay for the nation's.4 million fast-food workers stands at.80 an hour. for tenesha hueston, a shift manager at a burger king in durham, n.c., a.10 minimum wage would be a godsend for her christmas shopping . she says her pay.75 an hour —is too meager for her to buy the gifts her children are hankering for: a bicycle for her 5-year-old son and a leapfrog tablet learning toy for her 4-year-old daughter. ms. hueston, 36 and recently divorced, does housecleaning on the side, and moved back into her father's house with her children last spring when burger king reduced her weekly hours.with a higher wage, ms. hueston said, "i'd be able to buy things. maybe i'd be able to move out of my father's house. maybe i could get off food stamps . maybe i could start giving back to the economy ."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|1|+1.463487|
|republican|1|+1.232655|
|washington|1|+1.085620|
|law|1|+1.065501|
|officials|1|+0.936693|
|gov|1|+0.838101|
|house|1|+0.791979|
|county|1|+0.777282|
|his|1|+0.764993|
|open|1|+0.688413|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|companies|1|-1.057476|
|union|1|-0.743593|
|are|1|-0.615550|
|low|1|-0.565177|
|much|1|-0.550219|
|workers|1|-0.532713|
|products|1|-0.528103|
|food|1|-0.526349|
|international|1|-0.499180|
|for|1|-0.486115|

### row_id=4043：sports → politics

confidence=0.978425

原文：

east canton, ohio — she was a soldier. she had seen combat in the desert. so why was she now standing on a driving range with a golf club in her hands trembling with fear at distant fireworks?she was at clearview golf club with a group of female military veterans for a program called clearview hope. they were here to learn golf together.nobody laughed when she cringed at the faraway pops and booms. nobody questioned her reaction. nobody mentioned post-traumatic stress disorder .they all understood. they were comrades, and they, too, knew fear.that bond of 50 female veterans in clearview hope, which stands for helping our patriots everywhere, drew a little tighter that night. and instinctively, when one stumbled, others picked her up.they had done it on battlefields and on foreign soil, so they could certainly do it on the manicured grass of a golf course in ohio ."our golf program is recreational, but for them, it's also therapeutic," said renee powell, who created the program in may 2011 at clearview, a family-owned course she operates with her brother, larry.clearview hope was started as a women's offshoot of the p.g.a. of america's p.g.a. hope program, which has at least a dozen chapters nationwide. that veterans' program sprung from the iowa give initiative, an acronym meaning golf for injured veterans everywhere.but even with numerous programs for veterans, there has been an absence of participation by women who served in the armed forces . women have not connected through traditional veteran networks .according to the united states department of veteran affairs, there are almost.3 million female veterans. in ohio alone, there are an estimated,000.powell, whose father served in world war ii and then built the family's golf course, is a former l.p.g.a. tour player. she had traveled to vietnam on a u.s.o. tour in 1971 to teach golf to soldiers for three weeks, so when the p.g.a. of america called to ask if she would host a free program in ohio for female veterans, she agreed."i looked at existing programs for veterans, and there was nothing especially for women," said powell, a p.g.a. of america member and an honorary member of the l.p.g.a. teaching and club professionals.powell asked one of her students, the army veteran hollis burkes, to help her find female veterans in northeast ohio . she also visited the department of veterans affairs clinic in canton to leave fliers for enrolled female veterans.the fliers announced the new group and invited it to a lunch meeting and free golf clinic at firestone country club . powell offered the veterans five weeks of free golf lessons, supplying clubs and balls at clearview. "i figured they'd parade us out on memorial day and then forget about us like people usually do," said arlinda mitchell, who served in the army reserve for 12 years, part of it in kuwait.nearly 25 women showed up for the group's first clinic. some had not seen one another in 20 years. many were not aware other female veterans lived in the area ."hardly anybody knew each other that first day, but then comradeship kicked in," said mindy cooper, a retired army captain . "it didn't matter if you were white or black, army or air force, truck drivers or communicators."when the golf lessons began a few weeks later at clearview, 15 women took part. some came as scouts for others, bringing additional veterans with them the next week. and after the sessions ended, the former soldiers were again surprised when powell announced plans for continuing group activities for the rest of the year — and beyond."this has been about bringing women veterans together to heal," said powell.their healing has included sharing their experiences. many of the women report feeling minimized or shunned for their military service . when mitchell returned from operation desert storm in, she endured a bitter divorce and isolated herself. she worked at a hospital from 5 a.m. to:30 p.m., and was rarely seen by her neighbors. but she was proud of the personalized desert storm ohio license plate on her car. once, when a male friend was driving it, a man walked up to him in a parking lot and thanked him for his military service ."my friend said, 'i'm not the veteran; she is,' and he pointed to me," mitchell said. "the man looked at me, turned and walked away."burkes, whose 26 years of army service included tours in kuwait, iraq and saudi arabia, now works as a police officer for canton. on patrol one day, she said, she was called to help locate a missing juvenile.burkes stood with the child's father, staring at a house where the child was possibly being held. the man, a former marine, wanted to kick down the front door and charge into the house. burkes reminded him they were in ohio, not iraq ."he said, 'what would you know about iraq ?' and i told him i had served there, and he said, 'you were never in iraq,' " burkes said. "i totally lost control of myself and called him everything but a child of god."burkes apologized and went back to looking for the missing child, but she was embarrassed by her reaction and angry at the man's words."some people diminish you as a woman veteran," she said. "you want to be evaluated for your merits and not devalued because of your gender."joining clearview hope gave beth whitmore a chance to deal with emotions she had suppressed since service as an air force intelligence officer during the vietnam war ."this group has restored a part of my spirit that has been very badly damaged for a long time," said whitmore, who is now a judge . "i'm so lucky, so grateful that i have been able to put aside the burden of rejection that i have carried for years."through golf, the veterans have both calmed the panic of ptsd and experienced the joy of helping a vision-impaired member learn to putt."we also let her drive the golf cart once," said barb hickman, the group's president .veterans who are single mothers are invited to bring their children. several members recently pooled money to buy a set of clubs for a child so she could play with her mother, a purple heart recipient.the group has plans for a family picnic in september, and powell says she hopes to create a junior program for the veterans' children. because clearview hope has become a model program for female veterans, the p.g.a. of america plans to support an expansion of similar programs in texas and tennessee .


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|house|1|+0.966385|
|judge|1|+0.866923|
|military|1|+0.828708|
|people|1|+0.712464|
|police|1|+0.649305|
|states|1|+0.594946|
|about|1|+0.521507|
|support|1|+0.521100|
|which|1|+0.516845|
|some|1|+0.504907|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|player|1|-1.304940|
|the|1|-1.013713|
|play|1|-0.827861|
|club|1|-0.826727|
|in|1|-0.749026|
|world|1|-0.718677|
|and|1|-0.633930|
|to|1|-0.619425|
|of|1|-0.537426|
|for|1|-0.488196|

### row_id=9498：business → politics

confidence=0.733767

原文：

washington — initial jobless claims fell to their lowest level last week since the spring of, the labor department said on thursday. or not.the reported figure, which estimated that jobless claims had dropped to,000, about,000 fewer than the week before, seemingly suggested that the economy was finally entering a self-sustaining recovery on the back of a healing job market .the number, however, is unreliable, the government said, skewed by upgrades on two state computer systems that caused those states to underreport claims. the total number of initial jobless claims is almost certainly higher than reported, though nobody knows the scope of the mismeasurement at this point.the data malfunction has called into question the accuracy of a major leading indicator, one scrutinized by investors, economists and policy makers alike. it also shined a light on the imperfect and often outdated systems that states and the federal government use to provide benefits to workers and cull data on the labor market and the broader economy — a situation that some experts warn might become even worse because of the $1 trillion in budget cuts spread over 10 years known as sequestration.the labor department would not confirm which two states had issues or guess as to the scope of the mismeasurement. but nevada confirmed that it had not reported complete claims data to the federal government because of a computer upgrade."when we get data, we have an obligation to put it out there," said jason kuruvilla of the labor department, explaining why the department did not wait rather than release incomplete data. he emphasized that the department did not recommend reading too much into any one week's figure, at any rate."one week is not a trend," he said. mr. kuruvilla said the two states that had misreported data would become more apparent after new state -level jobless claims data were released next week.but some outside experts had scathing words for the labor department, and others described the data problem as not a one-time issue but a symptom of a chronic lack of money for one of the most critical functions of the government .rick mchugh of the national employment law project, a nonprofit group in washington, noted that unemployment insurance programs are partly financed by the federal government but administered by the states ."this is a symptom of a longstanding problem with the unemployment insurance programs," mr. mchugh said. "these are state agencies, but they're funded by federal dollars . and governors don't see them as their agencies. they're orphans."many state unemployment agencies have struggled to keep up with the demands of their rapidly expanding and changing rolls through the recession and the tepid recovery .sequestration has only made matters worse, as benefit cuts this year for the long-term unemployed required state to retool their systems.nevada has struggled to carry out the across-the- board 5 percent cut to a federally financed program for the long-term jobless. states that put the cut in place partway through the fiscal year, which ends on sept. 30, trimmed many recipients' benefit checks about 11 percent. nevada, which cut its checks only recently, did so by nearly 60 percent.problems with the computer system caused the mixup in reporting, said mae worthey, a public information officer with the nevada government . "it wasn't a glitch," she said. "it was just implementing a new system."economists said the reporting problems made it harder for experts and officials to keep track of the economy . that is especially critical now, as the federal reserve prepares for a crucial policy meeting next week." officials should be completely transparent when they know that bureaucratic issues are distorting their data," wrote justin wolfers of the brookings institution . "such transparency would allow economists to provide simple statistical fixes, making the data more reliable and useful."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|1|+1.463487|
|washington|1|+1.085620|
|law|1|+1.065501|
|officials|1|+0.936693|
|he|1|+0.917328|
|programs|1|+0.735020|
|mr|1|+0.540515|
|said|1|+0.508946|
|insurance|1|+0.467373|
|year|1|+0.452250|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|market|1|-1.121527|
|are|1|-0.615550|
|rate|1|-0.566856|
|much|1|-0.550219|
|investors|1|-0.538273|
|fell|1|-0.533073|
|workers|1|-0.532713|
|its|1|-0.529711|
|labor|1|-0.510605|
|for|1|-0.486115|

### row_id=5957：business → politics

confidence=0.824668

原文：

san francisco — california drillers eager to use hydraulic fracturing to tap the nation's largest oil shale formation will face comprehensive regulation for the first time next year under rules issued this week.the rules take effect on jan . 1, though they will be replaced a year later by permanent regulations that are still being developed but are expected to be similar. in september, gov . jerry brown signed a law that established the outlines for the regulations.the new rules require drillers to alert neighboring landowners at least 30 days before using hydraulic fracturing techniques, known as fracking, and to test their water wells upon request. the drillers must do other groundwater monitoring and also disclose many of the chemicals used. the rules cover the use of acids, which are sometimes used to dissolve rock to access oil .the rules cover many phases of the drilling process, analysts say, though they fall short of what many environmental groups want."there's definitely a tension in california between environmental groups who would like to see the practice halt, at least until there's a lot more research, and folks who would like to see it continue basically unregulated," said emily murray, a los angeles -based partner at the law firm allen matkins, whose clients hold a range of views on fracking.california's approach to fracking, she added, is "certainly short of banning the practice, but it's a pretty thorough look."the regulations are being imposed at a time when many states are moving to tighten restrictions on fracking, which is the extraction of oil or natural gas out of underground rocks by the use of a high-pressure mix of water, sand and chemicals . california is already the nation's third-largest oil producing state, but production has recently been flat, unlike surging north dakota and texas .a formation known as the monterey shale that lies beneath bakersfield and other central and southern california areas is believed to hold about two-thirds of the nation's recoverable shale oil, according to an estimate by the federal energy information administration . drillers are eager to tap the oil in the shale, but environmentalists fear that water and air pollution could result, and they are also concerned about the possibility of earthquakes linked to the disposal of fracking fluids.even though fracking has been taking place in california for decades, it has been stymied by the uneven and complex geology of the monterey shale . some say the geological challenges could even thwart major long-term development. california frackers are already subject to standard rules for drillers, like a mandatory review of the design of oil and gas wells. but the rise of fracking, with its special liquid chemical blend, has prompted calls for extra oversight. the rules governing the design of wells, for example, will be enhanced with new testing requirements.catherine reheis-boyd, president of the western states petroleum association, said that california's new rules were more comprehensive than any other state's. "i think it covers every possible area that one could think of," she said. the industry accepts the new regulations, she added.the permanent rules will include more specific groundwater monitoring requirements, and also make it easier for the state to say no to drillers if their paperwork is inadequate.over all, however, "there won't be a huge change between what they're doing between 2014 and," said jason marshall, the chief deputy director of california's department of conservation, which oversees the state's oil and gas regulatory division. the public will have a chance to attend hearings and comment.the rules do not go as far as the state's environmental lobbyists would like. on thursday, more than 100 environmental groups sent a letter to california coastal regulators urging a stop to offshore fracking. with fracking, "the risks of oil spills, vessel traffic, discharges of toxic waste, and air pollution are substantially increased," the groups wrote.on dec. 19, a court in california is scheduled to hear a case brought against state regulators by several environmental groups that want fracking to go through an environmental review process before it is allowed to continue. california plans to complete two major studies by july.essentially, "they're greenlighting fracking for the next year," said will rostov, a staff lawyer for earthjustice in california, which represents the environmental groups in the case . he added, "they're not doing the environmental analysis that needs to be done."he said new york had a better approach. fracking in the natural gas -rich marcellus shale is being delayed in new york until the state completes a health and environmental review . "you need to study it before you allow it," mr. rostov said.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|1|+1.463487|
|law|1|+1.065501|
|he|1|+0.917328|
|texas|1|+0.910897|
|gov|1|+0.838101|
|groups|1|+0.575828|
|mr|1|+0.540515|
|said|1|+0.508946|
|several|1|+0.506649|
|who|1|+0.489029|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|industry|1|-0.792309|
|are|1|-0.615550|
|regulatory|1|-0.573132|
|chief|1|-0.563369|
|production|1|-0.533412|
|its|1|-0.529711|
|for|1|-0.486115|
|oil|1|-0.437791|
|an|1|-0.431396|
|energy|1|-0.422806|

## count：15 个错误

### row_id=6332：politics → business

confidence=0.997907

原文：

washington — medicare beneficiaries can sign up for private health plans starting tuesday, but federal officials fear that many of them, out of confusion, might go to the new federal insurance exchange .in fact, people with medicare generally cannot buy insurance through the exchange . policies sold there duplicate many benefits provided by medicare, and it is illegal for insurance companies, agents and brokers to sell such polices to people known to have medicare, federal officials said monday.more than one-fourth of the 52 million medicare beneficiaries are in private managed care plans known as medicare advantage, and the obama administration is giving these insurance companies a fresh infusion of federal money .earlier this year, the administration reversed a proposed cut in federal payments to medicare advantage plans and decided — despite the recommendations of career government officials — to increase payments to them in. the decision followed extensive lobbying by the insurance industry . medicare actuaries estimate that as a result payments to insurers will rise by.5 billion in 2014 and by $60 billion over 10 years. those numbers include additional premiums that will be paid by medicare beneficiaries, roughly.5 billion next year and $14 billion over 10 years.joan m. jenness, 81, a retired schoolteacher who lives in bridgton, me., said she had been watching the rollout of the federal exchange "with fascination, muted horror and sympathy" for people struggling to use it."i am very glad that i do not have to worry about the exchange and health plans offered on the exchange, with their limited networks of doctors and hospitals," said ms. jenness, who added that her experience with medicare had been "very satisfactory."in a bulletin for older americans, the obama administration emphasized that people on medicare did not have to worry about the exchanges, or marketplaces, where millions of americans have been trying to shop for private insurance since oct. 1.the medicare handbook, sent to beneficiaries last month, drove home the point, saying, " medicare isn't part of the marketplace ."during the annual open enrollment period, which begins tuesday, medicare beneficiaries can sign up for medicare advantage plans offered by insurers like unitedhealth and humana and by blue cross and blue shield companies .a recent government notice to medicare beneficiaries says: "the health insurance marketplace is designed to help people who don't have any health insurance . you have health insurance through medicare . the marketplace won't have any effect on your medicare coverage ."the open enrollment period for medicare runs to dec. 7 and overlaps with the open enrollment period for the exchanges, which is from oct. 1 through march.to minimize confusion, the administration said that people on medicare "should make sure that they are reviewing medicare plans and not marketplace options."the potential for confusion is substantial. a number of insurers have used the terms "gold," "silver" or "platinum" for products sold to medicare beneficiaries, and similar terms are now used in the exchange .humana gold plus is the name of a health maintenance organization for medicare beneficiaries . coventry health care, acquired this year by aetna, offers medicare h.m.o.'s known as advantra silver and gold advantage.anne m. armao, a vice president of summacare, in akron, ohio, said the company had changed the names of its silver and gold medicare advantage plans to sapphire and emerald to avoid confusion with products offered on the exchange to people under.in newspaper advertisements intended for medicare beneficiaries last week, bruce d. broussard, the chief executive of humana, said: "we want to reassure you that these changes won't affect how you enroll in medicare . so you can relax — there's no need to worry."humana has reason to be concerned about public confusion: it derives more than 60 percent of its revenue — $25 billion of $39 billion last year — from medicare advantage .judith a. stein, the executive director of the nonprofit center for medicare advocacy, said she had received many calls from beneficiaries who believed incorrectly that "because of obamacare they have to make some change or have to go to the new marketplace ."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|medicare|29|+10.331685|
|plans|7|+1.655126|
|companies|3|+1.160990|
|in|11|+1.056400|
|that|10|+1.052108|
|is|6|+0.835280|
|company|1|+0.759673|
|are|3|+0.755793|
|billion|6|+0.745538|
|known|3|+0.615344|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|insurance|9|-2.372660|
|exchange|7|-1.500483|
|for|13|-1.395800|
|said|7|-1.316302|
|the|35|-1.165546|
|federal|6|-1.110625|
|obama|2|-1.093915|
|officials|3|-0.913032|
|open|3|-0.683210|
|health|7|-0.676685|

### row_id=6531：business → politics

confidence=0.532063

原文：

washington — the supreme court heard arguments on wednesday in a major labor case that, depending on how it is resolved, could hamper the ability of unions to mount successful campaigns to organize workers.the case concerns deals in which employers aid unionization drives in exchange for labor peace, sometimes called "neutrality agreements." several justices seemed receptive to the idea that such deals could run afoul of a federal labor law that bars employers from giving a "thing of value" to unions . chief justice john g . roberts jr . seemed skeptical of deals that include " card check" arrangements, in which employers allow unions to collect cards from workers saying they want a union, rather than putting the question to a secret vote.voluntary agreements to join a union are one thing, the chief justice said, while a deal between an employer and union allowing elections by card check "taints that process, in particular by allowing the card check procedure that it has been argued exercises coercion against employees to support the union."other justices seemed wary of interpreting the federal law too literally. justice anthony m . kennedy said that a strict reading of the law would be "contrary to years of settled practices and understandings ."as part of the arrangements at issue in the case, unite here local 355 v. mulhall, no. 12-99, a florida racetrack and casino, mardi gras gaming, agreed to provide information about its workers to the union, to permit organizers onto its grounds, to allow the card check procedure and to remain neutral.in exchange, the union agreed to spend more than,000 to support a casino gambling ballot initiative and not to picket or strike against mardi gras during the unionization drive.such arrangements are commonplace in the hospitality business, said richard g. mccracken, a lawyer for the union. "they are efficient," he said of the deals. "they avoid the hard feelings that come in many contested organizing campaigns and thereby create a good environment for collective bargaining."mr. mccracken said a ruling banning neutrality agreements would be "extremely damaging."but justice samuel a. alito jr . said that some of what the union agreed to provide fit comfortably within the usual definition of a "thing of value.""why wouldn't the right to use private property in a way that otherwise wouldn't be allowed constitute a thing of value?" he asked.mr. mccracken responded that a right of access is not a true property right but something less tangible.his main adversary, william l. messenger, a lawyer for martin mulhall, a worker who had objected to the agreement between the casino and the union, said that allowing such deals during organizing campaigns "would tear a massive hole" in the federal labor law . the law bans gifts from employers to unions, he said, and it should be enforced.michael r. dreeben, a deputy solicitor general, argued for the federal government in support of the union. he said the phrase "thing of value," read in isolation, could apply to some of what the casino had promised to do. but the law's other provisions and the general policy behind it, he said, favor sensible ground rules for organizing campaigns and allow neutrality agreements. justice elena kagan agreed with that expansive view of what is permissible in negotiations between employers and unions ."i would have thought that the premise and the policies of the labor laws are to encourage a wide variety of employer-employee agreements," she said. "the idea is to get these parties together to reach agreements on a wide variety of things that matter to them." justice stephen g . breyer urged the court to be practical. "you don't have to get into a metaphysical argument about 'things of value,' " he said."lists, access, promises to stay neutral are central to many aspects of organizing campaigns," he said. "to throw them in here is going to create a mess."still, justice sonia m. sotomayor said she was troubled by the money that the union had agreed to spend. "tell me how i deal with that niggling problem i have about the,000, because it does feel like a bribe to the employer," she said.mr. mccracken said it was commonplace for unions to work to expand their employers' businesses out of self-interest. "they do it because they want the jobs," he said.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|said|17|+3.196733|
|law|6|+2.522085|
|justice|7|+1.998998|
|he|8|+1.526242|
|the|44|+1.465258|
|they|5|+1.326244|
|be|5|+0.896198|
|for|7|+0.751584|
|federal|4|+0.740416|
|here|2|+0.619720|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|union|11|-3.853869|
|that|17|-1.788583|
|employers|6|-1.532489|
|in|15|-1.440546|
|are|5|-1.259655|
|labor|5|-1.188956|
|to|37|-0.790533|
|agreements|6|-0.726444|
|is|5|-0.696066|
|chief|2|-0.644712|

### row_id=6999：business → politics

confidence=0.907898

原文：

weeks of frantic technical work appear to have made the government's health care website easier for consumers to use. but that does not mean everyone who signs up for insurance can enroll in a health plan .the problem is that the systems that are supposed to deliver consumer information to insurers still have not been fixed. and with coverage for many people scheduled to begin in just 30 days, insurers are worried the repairs may not be completed in time."until the enrollment process is working from end to end, many consumers will not be able to enroll in coverage," said karen m. ignagni, president of america's health insurance plans, a trade group .the issues are vexing and complex. some insurers say they have been deluged with phone calls from people who believe they have signed up for a particular health plan, only to find that the company has no record of the enrollment. others say information they received about new enrollees was inaccurate or incomplete, so they had to track down additional data — a laborious task that will not be feasible if data is missing for tens of thousands of consumers .in still other cases, insurers said, they have not been told how much of a customer's premium will be subsidized by the government, so they do not know how much to charge the policyholder.in trying to fix healthcare. gov, president obama has given top priority to the needs of consumers, assuming that arrangements with insurers can be worked out later. the white house announced on sunday that it had met its goal for improving healthcare. gov so the website "will work smoothly for the vast majority of users ."in effect, the administration gave itself a passing grade. because of hundreds of software fixes and hardware upgrades in the last month, it said, the website — the main channel for people to buy insurance under the 2010 health care law — is now working more than 90 percent of the time, up from 40 percent during some weeks in october.jeffrey d. zients, the presidential adviser leading the repair effort, said he had shaken up management of the website so the team was now "working with the velocity and discipline of a high-performing private sector company ."mr. zients said,000 people could use the website at the same time and that the error rate, reflecting the failure of web pages to load properly, was consistently less than 1 percent, down from 6 percent before the overhaul.pages on the site generally load faster, in less than a second, compared with an average of eight seconds in late october, mr. zients said.whether mr. obama can fix his job approval ratings as well as the website is unclear. public opinion polls suggest he may have done more political damage to himself in the last two months than republican attacks on the health care law did in three years.people who have tried to use the website in the last few days report a mixed experience, with some definitely noticing improvements."every week, it's been getting better," said lynne m. thorp, who leads a team of counselors, or navigators, in southwestern florida . "it's getting faster, and nobody's getting kicked out."but neither mr. zients nor the department of health and human services indicated how many people were completing all the steps required to enroll in a health plan through the federal site, which serves residents of 36 states .and unless enrollments are completed correctly, coverage may be in doubt.for insurers the process is maddeningly inconsistent. some people clearly are being enrolled. but insurers say they are still getting duplicate files and, more worrisome, sometimes not receiving information on every enrollment taking place ." health plans can't process enrollments they don't receive," said robert zirkelbach, a spokesman for america's health insurance plans .despite talk from time to time of finding some sort of workaround, experts say insurers have little choice but to wait for the government to fix these problems. the insurers are in "an unenviable position," said brett graham, a managing director at leavitt partners, which has been advising states and others on the exchanges . "although they don't have the responsibility or the capability to fix the system, they're reliant on it."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|they|10|+2.652487|
|said|9|+1.692388|
|the|46|+1.531861|
|for|11|+1.181061|
|plan|3|+1.120762|
|obama|2|+1.093915|
|be|6|+1.075438|
|insurance|4|+1.054515|
|health|10|+0.966694|
|law|2|+0.840695|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|are|7|-1.763518|
|in|18|-1.728655|
|company|2|-1.519346|
|that|8|-0.841686|
|is|6|-0.835280|
|percent|4|-0.802017|
|than|4|-0.714433|
|plans|3|-0.709340|
|consumers|4|-0.657738|
|much|2|-0.557504|

### row_id=10419：politics → business

confidence=0.659487

原文：

vidalia, ga. — for years, labor unions and immigrant rights activists have accused large-scale farmers, like those harvesting sweet vidalia onions here this month, of exploiting mexican guest workers . working for hours on end under a punishing sun, the pickers are said to be crowded into squalid camps, driven without a break and even cheated of wages.but as congress weighs immigration legislation expected to expand the guest worker program, another group is increasingly crying foul — americans, mostly black, who live near the farms and say they want the field work but cannot get it because it is going to mexicans. they contend that they are illegally discouraged from applying for work and treated shabbily by farmers who prefer the foreigners for their malleability."they like the mexicans because they are scared and will do anything they tell them to," said sherry tomason, who worked for seven years in the fields here, then quit. last month she and other local residents filed a federal lawsuit against a large grower of onions, stanley farms, alleging that it mistreated them and paid them less than it paid the mexicans.the suit is one of a number of legal actions containing similar complaints against farms, including a large one in moultrie, ga., where americans said they had been fired because of their race and national origin, given less desirable jobs and provided with fewer work opportunities than mexican guest workers . under a consent decree with the equal employment opportunity commission, the farm, southern valley, agreed to make certain changes.with local unemployment about 10 percent and the bureaucracy for hiring foreigners onerous — guest workers have to be imported and housed and require extensive paperwork — it would seem natural for farmers to hire from their own communities, which they did a generation ago.in fact, the farmers say, they would dearly like to."we have tried to fill our labor locally," said brian stanley, an owner of stanley farms, which is being sued by ms. tomason and others. "but we couldn't get enough workers, and that was hindering our growth . so we turned to the guest worker program ."the vast majority of farm workers in the country are not in the guest worker program but are simply unauthorized immigrants . the plan to place those workers on a path to legal status would reduce the chances of their being exploited, the bill's sponsors say, and thereby also improve the status of americans who feel they cannot compete against vulnerable foreigners.mr. stanley, like other farmers, argues that americans who say they want the work end up quitting because it is hard, leaving the crops to rot in the fields. but the situation is filled with cultural and racial tensions .even many of the americans who feel mistreated acknowledge that the mexicans who arrive on buses for a limited period are incredibly efficient, often working into the night seven days a week to increase their pay."we are not going to run all the time," said henry rhymes, who was fired — unfairly, he says — from southern valley after a week on the job. "we are not mexicans.""when jose gets on the bus to come here from mexico he is committed to the work," he said. "it's like going into the military . he leaves his family at home. the work is hard, but he's ready. a domestic wants to know: what's the pay? what are the conditions? in these communities, i am sorry to say, there are no fathers at home, no role models for hard work. they want rewards without input."such generalizations lead lawyers — and residents — to say there are racist undertones to the farms' policies."i am not arguing that agricultural work is a good job," said dawson morton, a lawyer who focuses on farm workers' rights at the georgia legal services program, a nonprofit law firm . "i am arguing that it could be a better job. if you want experienced people, train them. just because people are easier to supervise, agricultural employers shouldn't be able to import them. it is not true that americans don't want the work. what the farmers are really saying is that blacks just don't want to work."to which j. larry stine, an atlanta lawyer for stanley farms and other big farms, replied: "the farmers are not racist or against americans. they have crops to be picked, and they see that domestics just don't have their hearts in it."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|are|14|+3.527035|
|work|10|+2.709403|
|is|11|+1.531346|
|want|6|+1.325191|
|their|6|+1.265078|
|that|10|+1.052108|
|in|8|+0.768291|
|them|5|+0.658015|
|month|2|+0.635834|
|job|3|+0.611433|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|they|14|-3.713482|
|the|41|-1.365354|
|said|7|-1.316302|
|who|9|-1.250821|
|for|10|-1.073692|
|americans|7|-1.064451|
|he|5|-0.953901|
|here|3|-0.929580|
|be|5|-0.896198|
|farm|3|-0.675353|

### row_id=6688：business → sports

confidence=0.779812

原文：

i'm a 24-year-old entrepreneur in mobile technologies. i haven't been flying for business all that long, but it's really important to my company's growth . i almost always leave home without doing much in terms of checking on my flight, having ground transportation or a hotel reserved. that may sound irresponsible, but i've found that mobile apps can do almost everything for me when i'm on the road.i first learned about how an app could really be helpful when i and several colleagues were working around the clock on a presentation for a client in los angeles . the presentation was planned for a wednesday. but monday afternoon, the client called and asked me to meet him in los angeles early tuesday morning . i needed to leave new york that afternoon if i had any shot of making the new meeting time.i left the office with only my laptop and my phone, and on the way to my apartment, i booked a ticket with an app and checked into my flight. i threw a few things into a bag, and then ran outside, hoping to catch a cab. but it was 4 p.m. and a shift change. there were no cabs in sight.i pulled up another app, booked a car, and was soon on my way to la guardia airport . i closed the deal the next day, and ever since i've been addicted to apps . i only wish there was an app to help me skip security .being a young guy, i really don't know that much about how to deal with children. on a recent flight from kennedy airport to beijing, i found myself sitting next to an 8-year-old boy. i'm not sure parents of six kids would know how to deal with him.just before taking off, the boy's father stood up from a few aisles away and mentioned casually to me, "just warning you. he's a talker."  i thought i could handle an 8-year-old. i was wrong. i had a 13- hour flight sitting next to probably the most curious juvenile on the planet.for the first few hours of the flight, the boy was playing loud video games . when those got old, he created the hilarious game of turning my reading light on and off to get a reaction from me. i tried being polite. i tried a semi-angry look. the little boy thought i was absolutely hysterical.his parents were oblivious to what was going on, chatting quietly before closing their eyes for a nap. lucky them. this boy was nonstop.during mealtime, he and i were served our appetizers, but for some reason the boy didn't receive his entree.   when i realized he had been skipped, i told the flight attendant he needed more food. at this point, i was midway through my dessert, and because of the language barrier, the flight attendant thought i said the boy needed another dessert. he got one. i was probably his hero.just as the boy had finished his first dessert and was moving onto his second, his mother woke up and came over to check on her child. she saw his empty dessert plate and then saw him diving into dessert no. 2. she started yelling at him in mandarin. though i speak a bit of mandarin, i stayed out of the conversation. i didn't want to get yelled at.she gave up and let her boy finish the second dessert. so now i'm stuck for the next five hours sitting next to an already talkative 8-year-old who is on a sugar high. good times. there wasn't an app invented that could save me.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|his|7|+2.525812|
|he|6|+1.680120|
|for|8|+1.432920|
|the|26|+1.260200|
|with|4|+1.061953|
|first|3|+0.938369|
|old|5|+0.926226|
|second|2|+0.741764|
|game|1|+0.646596|
|from|3|+0.606873|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|flight|7|-3.050597|
|that|6|-1.488277|
|my|9|-1.382165|
|me|6|-1.130275|
|an|7|-1.049888|
|of|8|-1.035803|
|to|19|-0.616488|
|about|2|-0.605163|
|company|1|-0.560369|
|and|17|-0.518251|

### row_id=4113：business → politics

confidence=0.999336

原文：

a group of state insurance commissioners emerged from a meeting with president obama and other federal officials on wednesday saying that state regulators would continue to decide on their own whether to go along with his recent proposal to let consumers keep older insurance plans for an extra year, even if the plans did not comply with regulations under the new health care law.in a conference call with reporters and in a statement issued after the meeting, they said they told the president they would not reach any consensus on what states should do. they said they warned the president that his proposal would amount to "different rules for different policies and might result in higher premiums for consumers without addressing underlying concern of gaps in coverage ."jim donelon, president of the national association of insurance commissioners and the louisiana insurance commissioner, said in a statement that members of his organization, which represents state insurance commissioners, "have been working to ensure that plans are compliant with the new rules."he added, "these proposed changes are creating a level of uncertainty that we must work together to alleviate." white house officials acknowledged that each state had to make the decision that was best for its consumers ." states have different populations with unique needs, and it is up to the insurance commissioner and health insurance companies to decide which insurance products can be offered to existing customers next year," the administration said in a statement.the meeting, which lasted 50 minutes, had a conciliatory tone, the regulators said, even as they declined to recommend a course of action to their counterparts across the country. the regulators said policy recommendations were not part of their mission."we share the president's goal of affordable coverage for consumers, and we will work with the insurance companies in our states to implement changes that make sense while following our mandate of consumer protection," mr. donelon said.mr. donelon attended the meeting with former senator ben nelson of nebraska, who is chief executive of the organization; the connecticut insurance commissioner, thomas b. leonardi; and the north carolina insurance commissioner, wayne goodwin. kathleen sebelius, the secretary of health and human services and the highest-ranking official overseeing the health care law, was also there.mr. obama announced his proposal days earlier, intending to make good on his often-repeated pledge that consumers who liked their insurance plans could keep them. despite his pledge, insurers have sent out cancellation notices to millions of people in recent weeks . the cancellations, which insurers attributed largely to the new health care requirements, had created anxiety among holders of health policies and was being used by political opponents to attack another aspect of the health care law .although the president urged insurers to renew older policies for another year, the decision is ultimately up to insurance companies, which write the policies, and state insurance regulators, who typically have final say over whether the old policies can be sold and what insurers can charge for them.some states, like florida, have said they will allow consumers to renew old policies, but others, including washington and indiana, have said they will not adopt mr. obama's proposal. new york has also said it will not comply with the president's request. california is to announce its decision on thursday.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|insurance|14|+3.690804|
|state|5|+2.197922|
|they|8|+2.121990|
|said|10|+1.880431|
|obama|3|+1.640872|
|law|3|+1.261043|
|states|4|+1.169287|
|president|7|+1.078159|
|the|32|+1.065642|
|his|6|+0.875984|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|companies|3|-1.160990|
|consumers|6|-0.986607|
|that|9|-0.946897|
|plans|4|-0.945786|
|regulators|4|-0.882681|
|their|4|-0.843386|
|decision|3|-0.795337|
|statement|3|-0.786214|
|in|8|-0.768291|
|its|2|-0.597813|

### row_id=6878：business → politics

confidence=0.765310

原文：

whatever the explanation, the states whose economies are most dependent on government employment and economic activity are also the states that are most likely to vote for republicans, who generally campaign on promises to reduce the size of government .consider one measure, the proportion of civilian employees in each state with government jobs, whether federal, state or local. nationally, the proportion last month was 16 percent, the lowest figure since.but the variance among the 50 states is large. at the top of the list, with one out of four workers employed by the government, is wyoming . at the other extreme is pennsylvania, with just one in eight. wyoming is among the most republican states, and that is part of a pattern. of the 15 states with the highest proportion of government employment, 10 voted for mitt romney, the republican nominee, in last year's presidential election . (the district of columbia, with more than 30 percent of the employees working for the government, is not included in the list because it is not a state, but it voted for president obama .) of the 15 states with the lowest level of government employment, only two — indiana and tennessee — voted for mr. romney .if only the 25 states with the lowest level of government employment had voted in the election, mr. obama would have won the national popular vote by a landslide margin of.3 percentage points, much larger than his actual margin of.9 percentage points . but among the other 25 states, plus the district of columbia, mr. romney had a.2 percentage point margin and would have easily won the election .the charts show state rankings on that and three other measures. the 15 states with the largest government involvement are at the top and the 15 with the lowest government involvement are at the bottom. states whose names are shaded voted for mr. romney and dominate all four of the top lists. states that voted for mr. obama are not shaded, and dominate the bottom lists. it should be noted that people may work in a different state from the one in which they live and vote. the ranking based on the proportion of government employees is shown in the left column of the chart. next to it is a ranking based on the increase or decline in total government employment since january, when the number of permanent government employees peaked. coincidentally, that was also the month that mr. obama took office .the other two are based on the state gross domestic product numbers calculated by the bureau of economic analysis of the commerce department . one shows the proportion resulting from government activity, rather than private sector activity, in, the most recent figure available. the next shows how much real government g.d.p. increased — or decreased — in the two years from 2010 to.a complete list of the figures for all 50 states, plus the district of columbia, can be found online with this column at at nytimes.com/ businessday .the state g.d.p. figures may well understate the importance of — and the decline in — government activity. that is because they are computed differently from the national g.d.p. number. the national number is based on spending, while the state numbers are based on profits and income of workers. as a result, if a government pays for the construction of something, whether a school or a fighter jet, that will show up as government activity in the national figure. but for the state figures, it will show up as private-sector activity because the work was done by employees of construction or aerospace companies .by the state figures, real government g.d.p. across the country fell by.3 percent during the two years through. the national g.d.p. figures, which reflect a substantial decline in local and state government investments in such things as schools and highways, showed a.2 percent decline, the largest for any two-year period since the early 1950s, when the government was demobilizing after the korean war .whether measured by g.d.p. or jobs, the last several years have been marked by an extraordinary reduction in government in most parts of the country.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|11|+4.835429|
|states|12|+3.507861|
|the|77|+2.564201|
|obama|4|+2.187830|
|for|11|+1.181061|
|national|5|+1.074174|
|republican|2|+1.027469|
|mr|6|+0.936559|
|they|2|+0.530497|
|years|3|+0.463881|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|are|10|-2.519311|
|government|22|-1.793595|
|in|17|-1.632619|
|is|11|-1.531346|
|at|6|-1.082181|
|based|5|-0.992942|
|that|9|-0.946897|
|percent|4|-0.802017|
|economic|2|-0.780365|
|on|8|-0.644266|

### row_id=7009：politics → business

confidence=0.792460

原文：

denver — hundreds of abandoned drilling wells dot eastern wyoming like sagebrush, vestiges of a natural gas boom that has been drying up in recent years as prices have plummeted.the companies that once operated the wells have all but vanished into the prairie, many seeking bankruptcy protection and unable to pay the cost of reclaiming the land they leased. recent estimates have put the number of abandoned drilling operations in wyoming at more than,200, and state officials said several thousand more might soon be orphaned by their operators . wyoming officials are now trying to address the problem amid concerns from landowners that the wells could contaminate groundwater and are a blight on the land.this month, gov . matt mead proposed allocating $3 million to pay for plugging the wells and reclaiming the land around them. and the issue is expected to be debated during next year's legislative session as lawmakers seek to hold drilling companies more accountable."the downturn in natural gas prices has forced small operators out of business, and the problem has really accelerated over the last couple of years," said the governor's policy director, shawn reese. " landowners would like their land to be brought back to a productive status and have orphaned wells cleaned up."drilling companies in wyoming typically lease land from the state, private owners or the federal bureau of land management, depending on who owns the mineral rights.the state's oil and gas conservation commission already budgets $1 million a year to plug abandoned wells. and under the governor's proposal, the commission would appropriate another $3 million over the next four years in an effort to restore property value and reduce the risk of contamination.the money would come from a conservation tax that oil and gas companies pay.still, given the number of wells already abandoned and the concern that more will soon be deserted, the money is not expected to go far. the state estimated that closing the,200 wells already abandoned would cost about $8 million .compounding the problem, state officials estimate that wyoming may also have to plug,300 wells that are sitting idle but have not been entirely abandoned by operators .there are also 400 idle wells scattered across land owned by the bureau of land management, which has its own criteria for determining when a well on its land is considered abandoned or idle. state officials said they would need to work with the bureau to help deal with those wells, too. governor mead also wants the commission, which he sits on, to review the conservation tax and bonding requirements for drilling companies to determine whether they are sufficient.currently, companies must pay a,000 blanket bond to cover all of the wells they operate — often numbering in the hundreds — on state and private land in wyoming . once a well stops producing and is deemed idle, the operator must pay up to $10 a linear foot in bonding to offset the cost of reclamation.but it is at that point that some companies drift into financial trouble and cannot pay the additional fees, leaving the state to scramble to make up the cost.the governor's proposal has drawn support from landowner groups like the powder river basin coalition, which has been pushing the state to take a tougher tack toward financially marginal drilling companies ."there has been a lot of hand-holding and coddling over the years when it comes to oil and gas operators and their ability to pay the bonding," said jill morrison, an organizer with the group.ms. morrison said that the issue had largely been ignored during wyoming's peak boom years — from 1995 to."we are really pleased there is an actual plan to move forward with an aggressive plugging and reclamation strategy," she said.the proposal is also backed by the petroleum association of wyoming, which favors raising the conservation tax to help pay for plugging fees. the group also supports higher bond fees for operators with tenuous finances ."it's how you weed out companies that are too risky to go into business with," said the group's president, bruce hinchey.but getting drilling companies who claim to be on the verge of collapse to take responsibility for wells they still technically own has proved difficult.one such company, patriot energy resources, which owns about 900 idle wells on state and private land, said in an october letter to governor mead that it was.9 million short of full bonding on those wells after the bankruptcy filing of luca technologies, its parent company .patriot has proposed allowing another drilling company to take on a part of its debt, saying it will have to abandon its wells otherwise. "without this deal or something similar, patriot will be forced to file for bankruptcy and turn these wells and reservoirs over to the state of wyoming," a company official wrote in the letter.renny mackay, a spokesman for mr. mead, said the state was weighing the offer. state senator john j. hines, a republican who represents mineral-rich campbell and converse counties, said it was vital for lawmakers to take up the issue swiftly, because natural gas was so important to wyoming's economy ."all of this just came to a head at once," said mr. hines, who heads the senate's minerals committee .last spring, mr. hines was told by patriot that the hum of gas drilling activity on his own sprawling cattle ranch would soon grow quiet.soon after, the company, which leased parcels of mr. hines's land, disappeared completely — leaving behind more than 40 coal -bed methane wells and a jumble of pipes and pumps."they informed me that they were shutting down because they were short of funds," mr. hines said. "all of it, in my opinion, needs to be cleaned up."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|companies|10|+3.869965|
|company|5|+3.798365|
|pay|8|+1.887238|
|are|7|+1.763518|
|that|15|+1.578161|
|its|5|+1.494533|
|oil|3|+1.064521|
|in|11|+1.056400|
|is|7|+0.974493|
|to|38|+0.811899|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|state|13|-5.714598|
|said|12|-2.256517|
|the|64|-2.131284|
|they|8|-2.121990|
|be|7|-1.254678|
|officials|4|-1.217376|
|for|9|-0.966323|
|governor|5|-0.925841|
|mr|5|-0.780466|
|years|5|-0.773134|

### row_id=4565：business → politics

confidence=0.998215

原文：

this spring, the missouri chamber of commerce urged the state legislature to accept the federal government's plan to expand medicaid for the poor and disabled.the business lobbying group had not suddenly gone rogue. here is how daniel p. mehan, its president, summarized his feelings about president obama's health care law : "we don't like it."but the chamber was cognizant of the plea of its members directly affected by the issue: dozens of missouri hospitals stood to lose.2 billion over six years in federal support for uncompensated care if the state refused to increase the income ceiling for medicaid eligibility.pragmatism suggested accepting the expansion. washington would pay the extra cost entirely for three years and pick up 90 percent of the bill thereafter.and it would expand health coverage in the state's poor, predominantly white rural counties, which voted consistently to put republican lawmakers into office.missouri's republican -controlled legislature — heavy with tea party stalwarts — rejected medicaid's expansion in the state anyway.after their vote, a frustrated editorial in the missourian, a faithfully conservative newspaper in washington, mo., asked of the state's elected republicans : "who do they represent?"today, the same forces that blocked the expansion of medicaid in missouri are going all out in washington in a bid to undo all of the affordable care act . bowing to the vehemence of its tea party faction, the house g.o.p. forced a government shutdown when senate democrats refused to delay or defund the president's health overhaul. house republicans are threatening even further damage if they don't get their way, possibly unleashing financial chaos if they manage to force the united states into its first default ever on the government's debt .republicans' efforts raise the same perplexing question posed by the missourian: what drives tea party republicans and their financial backers ? what calculation persuades them that repealing the health care law is worth the risk ? indeed, whose interests do they represent?nearly 6 in 10 americans disapprove of trying to stop the law by cutting its financing . even among those who don't like the law, less than half want their representatives in congress to try to make it fail.it is tempting to discard the tea party activists driving the republican party as crazy — as some commentators have — motivated by fear and willing to believe that default won't cause much harm and might even act as a purgative to free the economy of a bloated government ."they listen to nobody but themselves," the harvard political scientist theda skocpol told me. "they are convinced of their rectitude and convinced that they alone are qualified to save america from the dire threat of obama and his polices. they have worked themselves into a dangerous place."their relationship with reality can take peculiar turns. reflexive opponents of " government," they can exhibit little sense of what the government actually does.and yet the argument that half the republican party has simply lost its mind has to be an unsatisfactory answer, especially considering the sophistication of some of the deep-pocketed backers of the tea party insurgency .there is a plausible alternative to irrationality. flawed though it may turn out to be, obamacare, as the affordable care act is popularly known, could fundamentally change the relationship between working americans and their government . this could pose an existential threat to the small- government credo that has defined the g.o.p. for four decades.the law is imperfect. it has dozens of complicated, interlocking parts. half of americans say they don't understand how it will affect them and their family. still, the law has many provisions that are likely to improve life for millions of americans, including a big portion of what we know as the working middle class .almost two-thirds of uninsured americans have a full-time job, according to the kaiser family foundation . a further 16 percent are employed part time.the department of health and human services recently estimated that nearly six in 10 uninsured americans could qualify for health coverage in the insurance market for less than $100 per person per month.according to an analysis by the urban institute, 28 million americans would gain health insurance under obamacare . of these, eight million earn more than twice the poverty level of,100 for a family of four. a majority of those would get a subsidy to buy a plan.as it turns out, the core tea party demographic — working white men between the ages of 45 and 64 — would do fairly well under the law.take missouri . it has about,000 uninsured. almost half of them would have been eligible for expanded medicaid benefits, had the legislature not rejected them. many of the rest — including families of four making up to,000 — will be eligible to get subsidized health insurance .in st . louis, for instance, a family of four making,000 a year will be able to buy a middle-of-the-road "silver" health plan for $282 a month and a bottom-end "bronze" plan for. even medicare recipients will get a benefit worth a few hundred dollars a year.in, when president bill clinton took an earlier stab at a health care overhaul, the conservative thinker william kristol published a manifesto about why republicans had to stop it." passage of the clinton health plan in any form would be disastrous," mr. kristol wrote, italicizing for emphasis. "it would guarantee an unprecedented federal intrusion into the american economy . its success would signal the rebirth of centralized welfare-state policy at the moment that such policy is being perceived as a failure in other areas."two decades after mr. clinton's ultimately failed attempt, obamacare poses the same sort of threat.even americans who say they dislike the law actually like many of its components. nearly three-quarters approve of giving financial help to poor and moderate- income americans to buy health insurance . two-thirds approve of barring insurance companies from denying coverage because of somebody's medical history . three-quarters favor letting children stay on their parents' insurance until they are.until now, social welfare programs in the united states have exhibited a "big hole," professor skocpol said, consisting of nonpoor working-age americans and their children. obamacare closes a big chunk of it."the main beneficiaries tend to have lower wages, employed in smaller businesses that are not providing health insurance," she said. "they are not elderly. they are also not the poorest."and they might be grateful to democrats for the benefit.to conservative republicans, losing a large slice of the middle class to the ranks of the democratic party could justify extreme measures.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|they|15|+3.978731|
|law|8|+3.362781|
|republicans|6|+2.703706|
|state|6|+2.637507|
|the|74|+2.464298|
|republican|4|+2.054938|
|plan|5|+1.867936|
|insurance|7|+1.845402|
|for|15|+1.610538|
|americans|10|+1.520644|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|are|10|-2.519311|
|its|8|-2.391253|
|their|10|-2.108464|
|in|18|-1.728655|
|that|10|-1.052108|
|is|7|-0.974493|
|financial|3|-0.858979|
|to|35|-0.747801|
|care|6|-0.684425|
|don|4|-0.669132|

### row_id=10714：business → politics

confidence=0.999730

原文：

as the obama administration's health overhaul sputters in its opening weeks, insurers and advocacy groups are pursuing a new strategy in the quest to get millions of young people to sign up for health insurance : they're appealing to their mothers.in one cheeky campaign, aarp is urging mothers to send e-cards to their children reminding them to sign up. one e- card reads, "as a reward for signing up for health insurance, i'll defriend you on facebook ." another group, organizing for action, is seeking to steer holiday conversations toward health care by encouraging parents to have "the talk" with their adult children . and a colorado group is promoting an ad featuring a hapless young man who calls his mother from the golf course: "yo, mom, do i got insurance ?"recruiting enough young people is a major goal of the obama administration because insurers need healthy customers to offset the cost of caring for those with expensive medical needs.the goal carries even more urgency now that insurers are considering a proposal by president obama to let people, many of them healthy, stay on their existing policies for another year. if fewer of those people buy insurance in the new marketplaces, signing up young people without insurance will be even more crucial. young people also account for a major chunk of the uninsured. about 40 percent of the estimated 41 million uninsured people nationwide who are eligible for coverage are between the ages of 18 and, according to the administration .even as supporters are enlisting mothers in the effort to sign up their adult children, critics have mounted an equally aggressive and well-funded campaign urging young people to "opt out" of coverage . opponents use many of the same marketing tools as the law's supporters, reaching out to young people on social media and through web videos. advocacy groups and insurers are expected to make a major marketing push beginning in early december, when the obama administration has said it expects the malfunctioning federal health care website to be working better. they have their targets set on two major deadlines: dec. 23, when insurance must be purchased for coverage beginning on jan. 1, and march, when the open enrollment period will end.beneath the marketing campaigns' playful language is a deeper truth: when it comes to making major life decisions, many people — especially young adults — still turn to their mothers for help. more broadly, women make about 80 percent of the health care decisions for their families, according to the federal labor department ."it's the cutest phenomenon ever," said lynn quincy, a senior health policy analyst at consumers union, who stumbled on the significance of mothers while conducting a focus group of men and women last year about how well people understood the language in their insurance policies . when asked who they turned to for advice about health care, the overwhelming answer was their mothers. "these people could have husbands, they could have fathers, they may have a nurse who lives next door, but they're all going to their moms," she said.of course, the administration and advocacy groups are also reaching out directly to young people themselves, collaborating with outlets like the comedy website funny or die, initiating social media campaigns, handing out fliers at concerts and sponsoring a video contest aimed at getting young people to sign up."people need to have heard about it a couple of times, and frankly from a couple of different sources," said jon carson, the executive director of organizing for action, the nonprofit group that grew out of president obama's 2012 campaign organization. he said mothers represented just one avenue that they hoped would help persuade a young person to enroll. the recently posted video is part of a campaign, called healthcare for the holidays, that seeks to arm parents with talking points when they see their children at family get-togethers.this approach may resonate especially well with the so-called millennial generation, which came of age in a recession and may still financially depend on their parents, say some experts."millennials love their parents and they count on them for advice," said morley winograd, the co-author of three books on the millennial generation . he noted that this might sound surprising to baby boomers, who famously rebelled against their parents' generation. but millennials "assume that their parents have more worldly experience, and know about things like money and health insurance," he said.mary babich, the mother of two children in their 20s without insurance, said she had been pestering both of them to sign up. "they look at it as just government bureaucracy — as almost akin to filling out their taxes," said ms. babich, who lives in wisconsin . she paused, and added, "the sad thing is, i've always done both of their taxes ."the mother-knows-best strategy isn't entirely new. in, when massachusetts introduced its health care law, officials mailed greeting cards, timed for mother's day, to the parents of young men between the ages of 18 and. market research had shown this group was among the most resistant to buying insurance . "the idea was to trigger a phone call from the parent to the child to say, 'hey, by the way, do you have insurance ?' " said kevin j. counihan, who served as chief marketing officer for massachusetts's health insurance marketplace at the time. "we made the hypothesis that we could best reach the young men through their mothers."the effort, mr. counihan said, was a moderate success: many parents decided to pick up the bill for their sons' health insurance . and more often than not, "we found they bought the most expensive plan because apparently nothing was too good for johnny." mr. counihan is now chief executive of connecticut's state marketplace and said he was still targeting the mothers of young men by focusing on churches and community groups where they are likely to be members. insurers are also taking note of this influence. shaun greene, the chief operating officer at arches health plan, a health care co-op in utah, said he was surprised during a recent televised call-in when he fielded several calls from parents who quickly handed the phone to their children. "at least three of them had their kid by the ear," he said, explaining: "my son or daughter needs insurance . talk to them."a certain level of concern is just part of being a parent, said nicole duritz, who helped develop the aarp campaign. "i'm a mom and i'm constantly worried about my kids, and making sure they're making good decisions," she said. "and health insurance falls into that category."that's certainly true for lynne jackier, of ithaca, n.y., who has been helping her 24-year-old daughter look into buying health insurance on the state marketplace . she also has a 26-year-old son who recently moved to california and is also uninsured."i feel like, as parents, it's our responsibility to get them to look at this now," ms. jackier said.her daughter, rosie simon, works as a nanny in westchester county and said she had been uninsured since graduating from college a few years ago . although ms. simon said that she had heard about the changes coming under the health care law, she added that her mother had been persistent in making sure she signed up. last weekend, during a visit home, the two sat down at the computer and took the initial steps of completing an application on new york's marketplace .without insurance, ms. simon said she often delayed going to the doctor when sick, or leaned on her parents for help. ms. jackier, who is on medicaid and so can't cover her daughter through private insurance, said she had become accustomed to the frustrating conversations. "she'll get sick and i'll say, 'you have go to the doctor,' " ms. jackier said. "and she'll say, 'well, i don't have insurance .' "the family had a scare when ms. simon recently developed a serious kidney infection. her parents paid the bill, which cost a few hundred dollars . it wasn't ideal, ms. simon said, but "i'm still their baby."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|insurance|19|+5.008948|
|said|23|+4.324991|
|they|13|+3.448233|
|obama|5|+2.734787|
|she|13|+2.587455|
|for|21|+2.254753|
|the|66|+2.197887|
|who|13|+1.806742|
|health|17|+1.643379|
|he|7|+1.335461|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|their|24|-5.060314|
|are|9|-2.267380|
|at|10|-1.803635|
|is|11|-1.531346|
|in|15|-1.440546|
|that|11|-1.157318|
|young|14|-1.144242|
|on|14|-1.127465|
|chief|3|-0.967068|
|to|44|-0.940093|

### row_id=3536：politics → business

confidence=0.654482

原文：

congress now has an array of legislative options to prevent the interest rate on student loans from doubling to.8 percent on july, as scheduled.with student loans topping.1 trillion — and held by one in five american households — many families are questioning why students should pay so much when market interest rates are so low.on thursday, representative john kline, a minnesota republican who is chairman of the house committee on education and the workforce, introduced legislation that would provide a long-term solution, tying interest rates to the government's cost of borrowing, as the obama administration proposed in its budget."i think a lot of people are going to go for it," mr. kline said. "i talked to secretary duncan yesterday," he added, referring to education secretary arne duncan, "and told him that our numbers were a little different, but the approach is the same."there are other proposals out there, too. in her first stand-alone legislation, senator elizabeth warren, democrat of massachusetts, introduced a bill on wednesday to cut the student loan rate for one year to.75 percent, the rate that big banks get.two other democratic senators and two democratic representatives this week proposed rates based on the 91-day treasury bill, and three republican senators have offered legislation that would set the interest rate at three percentage points above the 10-year treasury rate.there is now widespread acceptance of the idea of moving to market -based rates. under mr. kline's proposal, students would pay the 10-year treasury rate, plus.5 percent, for all stafford loans, with a cap of.5 percent. for parent plus and grad plus loans, the rate would be the treasury rate plus.5 percent, with a.5 percent cap.real divisions remain, though. the administration proposed no cap on interest, leaving students vulnerable to high rates in years to come. but while the white house wants rates fixed for the life of the loan, the kline bill would reset rates each year — and that, too, would leave students vulnerable to high costs if interest rates rise .in a statement thursday afternoon, the president again called for congress to act to prevent the rate from doubling, but did not endorse mr. kline's plan."while we welcome action by the house on student loans, we have concerns about an approach that both fails to guarantee low rates for students on july 1 and asks too many of them to bear the burden of deficit reduction through unaffordable rates," said the statement, from a spokesman, matt lehrich.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|rate|9|+1.549217|
|percent|6|+1.203025|
|are|4|+1.007724|
|market|2|+0.831883|
|on|9|+0.724799|
|that|6|+0.631265|
|statement|2|+0.524143|
|in|5|+0.480182|
|pay|2|+0.471809|
|too|3|+0.462481|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|students|5|-1.508336|
|republican|2|-1.027469|
|the|26|-0.865834|
|for|7|-0.751584|
|obama|1|-0.546957|
|mr|3|-0.468280|
|year|4|-0.433200|
|there|3|-0.404551|
|plus|4|-0.402988|
|democratic|2|-0.391561|

### row_id=4043：sports → politics

confidence=0.820540

原文：

east canton, ohio — she was a soldier. she had seen combat in the desert. so why was she now standing on a driving range with a golf club in her hands trembling with fear at distant fireworks?she was at clearview golf club with a group of female military veterans for a program called clearview hope. they were here to learn golf together.nobody laughed when she cringed at the faraway pops and booms. nobody questioned her reaction. nobody mentioned post-traumatic stress disorder .they all understood. they were comrades, and they, too, knew fear.that bond of 50 female veterans in clearview hope, which stands for helping our patriots everywhere, drew a little tighter that night. and instinctively, when one stumbled, others picked her up.they had done it on battlefields and on foreign soil, so they could certainly do it on the manicured grass of a golf course in ohio ."our golf program is recreational, but for them, it's also therapeutic," said renee powell, who created the program in may 2011 at clearview, a family-owned course she operates with her brother, larry.clearview hope was started as a women's offshoot of the p.g.a. of america's p.g.a. hope program, which has at least a dozen chapters nationwide. that veterans' program sprung from the iowa give initiative, an acronym meaning golf for injured veterans everywhere.but even with numerous programs for veterans, there has been an absence of participation by women who served in the armed forces . women have not connected through traditional veteran networks .according to the united states department of veteran affairs, there are almost.3 million female veterans. in ohio alone, there are an estimated,000.powell, whose father served in world war ii and then built the family's golf course, is a former l.p.g.a. tour player. she had traveled to vietnam on a u.s.o. tour in 1971 to teach golf to soldiers for three weeks, so when the p.g.a. of america called to ask if she would host a free program in ohio for female veterans, she agreed."i looked at existing programs for veterans, and there was nothing especially for women," said powell, a p.g.a. of america member and an honorary member of the l.p.g.a. teaching and club professionals.powell asked one of her students, the army veteran hollis burkes, to help her find female veterans in northeast ohio . she also visited the department of veterans affairs clinic in canton to leave fliers for enrolled female veterans.the fliers announced the new group and invited it to a lunch meeting and free golf clinic at firestone country club . powell offered the veterans five weeks of free golf lessons, supplying clubs and balls at clearview. "i figured they'd parade us out on memorial day and then forget about us like people usually do," said arlinda mitchell, who served in the army reserve for 12 years, part of it in kuwait.nearly 25 women showed up for the group's first clinic. some had not seen one another in 20 years. many were not aware other female veterans lived in the area ."hardly anybody knew each other that first day, but then comradeship kicked in," said mindy cooper, a retired army captain . "it didn't matter if you were white or black, army or air force, truck drivers or communicators."when the golf lessons began a few weeks later at clearview, 15 women took part. some came as scouts for others, bringing additional veterans with them the next week. and after the sessions ended, the former soldiers were again surprised when powell announced plans for continuing group activities for the rest of the year — and beyond."this has been about bringing women veterans together to heal," said powell.their healing has included sharing their experiences. many of the women report feeling minimized or shunned for their military service . when mitchell returned from operation desert storm in, she endured a bitter divorce and isolated herself. she worked at a hospital from 5 a.m. to:30 p.m., and was rarely seen by her neighbors. but she was proud of the personalized desert storm ohio license plate on her car. once, when a male friend was driving it, a man walked up to him in a parking lot and thanked him for his military service ."my friend said, 'i'm not the veteran; she is,' and he pointed to me," mitchell said. "the man looked at me, turned and walked away."burkes, whose 26 years of army service included tours in kuwait, iraq and saudi arabia, now works as a police officer for canton. on patrol one day, she said, she was called to help locate a missing juvenile.burkes stood with the child's father, staring at a house where the child was possibly being held. the man, a former marine, wanted to kick down the front door and charge into the house. burkes reminded him they were in ohio, not iraq ."he said, 'what would you know about iraq ?' and i told him i had served there, and he said, 'you were never in iraq,' " burkes said. "i totally lost control of myself and called him everything but a child of god."burkes apologized and went back to looking for the missing child, but she was embarrassed by her reaction and angry at the man's words."some people diminish you as a woman veteran," she said. "you want to be evaluated for your merits and not devalued because of your gender."joining clearview hope gave beth whitmore a chance to deal with emotions she had suppressed since service as an air force intelligence officer during the vietnam war ."this group has restored a part of my spirit that has been very badly damaged for a long time," said whitmore, who is now a judge . "i'm so lucky, so grateful that i have been able to put aside the burden of rejection that i have carried for years."through golf, the veterans have both calmed the panic of ptsd and experienced the joy of helping a vision-impaired member learn to putt."we also let her drive the golf cart once," said barb hickman, the group's president .veterans who are single mothers are invited to bring their children. several members recently pooled money to buy a set of clubs for a child so she could play with her mother, a purple heart recipient.the group has plans for a family picnic in september, and powell says she hopes to create a junior program for the veterans' children. because clearview hope has become a model program for female veterans, the p.g.a. of america plans to support an expansion of similar programs in texas and tennessee .


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|veterans|19|+3.930933|
|of|28|+3.719677|
|said|14|+2.082064|
|she|21|+1.712949|
|they|8|+1.447090|
|military|3|+1.336889|
|were|7|+1.273897|
|women|8|+1.219592|
|years|4|+1.072715|
|that|7|+0.999848|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|at|13|-3.860673|
|golf|13|-3.504508|
|club|4|-2.355681|
|in|24|-2.268749|
|with|9|-2.052386|
|for|26|-1.865391|
|when|7|-1.292282|
|has|8|-1.151949|
|also|3|-0.707922|
|the|46|-0.697723|

### row_id=9498：business → politics

confidence=0.676283

原文：

washington — initial jobless claims fell to their lowest level last week since the spring of, the labor department said on thursday. or not.the reported figure, which estimated that jobless claims had dropped to,000, about,000 fewer than the week before, seemingly suggested that the economy was finally entering a self-sustaining recovery on the back of a healing job market .the number, however, is unreliable, the government said, skewed by upgrades on two state computer systems that caused those states to underreport claims. the total number of initial jobless claims is almost certainly higher than reported, though nobody knows the scope of the mismeasurement at this point.the data malfunction has called into question the accuracy of a major leading indicator, one scrutinized by investors, economists and policy makers alike. it also shined a light on the imperfect and often outdated systems that states and the federal government use to provide benefits to workers and cull data on the labor market and the broader economy — a situation that some experts warn might become even worse because of the $1 trillion in budget cuts spread over 10 years known as sequestration.the labor department would not confirm which two states had issues or guess as to the scope of the mismeasurement. but nevada confirmed that it had not reported complete claims data to the federal government because of a computer upgrade."when we get data, we have an obligation to put it out there," said jason kuruvilla of the labor department, explaining why the department did not wait rather than release incomplete data. he emphasized that the department did not recommend reading too much into any one week's figure, at any rate."one week is not a trend," he said. mr. kuruvilla said the two states that had misreported data would become more apparent after new state -level jobless claims data were released next week.but some outside experts had scathing words for the labor department, and others described the data problem as not a one-time issue but a symptom of a chronic lack of money for one of the most critical functions of the government .rick mchugh of the national employment law project, a nonprofit group in washington, noted that unemployment insurance programs are partly financed by the federal government but administered by the states ."this is a symptom of a longstanding problem with the unemployment insurance programs," mr. mchugh said. "these are state agencies, but they're funded by federal dollars . and governors don't see them as their agencies. they're orphans."many state unemployment agencies have struggled to keep up with the demands of their rapidly expanding and changing rolls through the recession and the tepid recovery .sequestration has only made matters worse, as benefit cuts this year for the long-term unemployed required state to retool their systems.nevada has struggled to carry out the across-the- board 5 percent cut to a federally financed program for the long-term jobless. states that put the cut in place partway through the fiscal year, which ends on sept. 30, trimmed many recipients' benefit checks about 11 percent. nevada, which cut its checks only recently, did so by nearly 60 percent.problems with the computer system caused the mixup in reporting, said mae worthey, a public information officer with the nevada government . "it wasn't a glitch," she said. "it was just implementing a new system."economists said the reporting problems made it harder for experts and officials to keep track of the economy . that is especially critical now, as the federal reserve prepares for a crucial policy meeting next week." officials should be completely transparent when they know that bureaucratic issues are distorting their data," wrote justin wolfers of the brookings institution . "such transparency would allow economists to provide simple statistical fixes, making the data more reliable and useful."


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|5|+2.197922|
|department|6|+2.019276|
|states|6|+1.753930|
|the|51|+1.698367|
|said|9|+1.692388|
|federal|5|+0.925520|
|washington|2|+0.914745|
|they|3|+0.795746|
|for|6|+0.644215|
|officials|2|+0.608688|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|week|6|-1.382189|
|that|12|-1.262529|
|labor|5|-1.188956|
|their|5|-1.054232|
|market|2|-0.831883|
|are|3|-0.755793|
|is|5|-0.696066|
|percent|3|-0.601513|
|than|3|-0.535825|
|systems|3|-0.516791|

### row_id=5957：business → politics

confidence=0.924548

原文：

san francisco — california drillers eager to use hydraulic fracturing to tap the nation's largest oil shale formation will face comprehensive regulation for the first time next year under rules issued this week.the rules take effect on jan . 1, though they will be replaced a year later by permanent regulations that are still being developed but are expected to be similar. in september, gov . jerry brown signed a law that established the outlines for the regulations.the new rules require drillers to alert neighboring landowners at least 30 days before using hydraulic fracturing techniques, known as fracking, and to test their water wells upon request. the drillers must do other groundwater monitoring and also disclose many of the chemicals used. the rules cover the use of acids, which are sometimes used to dissolve rock to access oil .the rules cover many phases of the drilling process, analysts say, though they fall short of what many environmental groups want."there's definitely a tension in california between environmental groups who would like to see the practice halt, at least until there's a lot more research, and folks who would like to see it continue basically unregulated," said emily murray, a los angeles -based partner at the law firm allen matkins, whose clients hold a range of views on fracking.california's approach to fracking, she added, is "certainly short of banning the practice, but it's a pretty thorough look."the regulations are being imposed at a time when many states are moving to tighten restrictions on fracking, which is the extraction of oil or natural gas out of underground rocks by the use of a high-pressure mix of water, sand and chemicals . california is already the nation's third-largest oil producing state, but production has recently been flat, unlike surging north dakota and texas .a formation known as the monterey shale that lies beneath bakersfield and other central and southern california areas is believed to hold about two-thirds of the nation's recoverable shale oil, according to an estimate by the federal energy information administration . drillers are eager to tap the oil in the shale, but environmentalists fear that water and air pollution could result, and they are also concerned about the possibility of earthquakes linked to the disposal of fracking fluids.even though fracking has been taking place in california for decades, it has been stymied by the uneven and complex geology of the monterey shale . some say the geological challenges could even thwart major long-term development. california frackers are already subject to standard rules for drillers, like a mandatory review of the design of oil and gas wells. but the rise of fracking, with its special liquid chemical blend, has prompted calls for extra oversight. the rules governing the design of wells, for example, will be enhanced with new testing requirements.catherine reheis-boyd, president of the western states petroleum association, said that california's new rules were more comprehensive than any other state's. "i think it covers every possible area that one could think of," she said. the industry accepts the new regulations, she added.the permanent rules will include more specific groundwater monitoring requirements, and also make it easier for the state to say no to drillers if their paperwork is inadequate.over all, however, "there won't be a huge change between what they're doing between 2014 and," said jason marshall, the chief deputy director of california's department of conservation, which oversees the state's oil and gas regulatory division. the public will have a chance to attend hearings and comment.the rules do not go as far as the state's environmental lobbyists would like. on thursday, more than 100 environmental groups sent a letter to california coastal regulators urging a stop to offshore fracking. with fracking, "the risks of oil spills, vessel traffic, discharges of toxic waste, and air pollution are substantially increased," the groups wrote.on dec. 19, a court in california is scheduled to hear a case brought against state regulators by several environmental groups that want fracking to go through an environmental review process before it is allowed to continue. california plans to complete two major studies by july.essentially, "they're greenlighting fracking for the next year," said will rostov, a staff lawyer for earthjustice in california, which represents the environmental groups in the case . he added, "they're not doing the environmental analysis that needs to be done."he said new york had a better approach. fracking in the natural gas -rich marcellus shale is being delayed in new york until the state completes a health and environmental review . "you need to study it before you allow it," mr. rostov said.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|state|7|+3.077091|
|rules|10|+2.405384|
|the|51|+1.698367|
|groups|6|+1.597991|
|they|6|+1.591492|
|said|7|+1.316302|
|for|9|+0.966323|
|be|5|+0.896198|
|law|2|+0.840695|
|california|13|+0.791586|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|oil|9|-3.193564|
|are|9|-2.267380|
|is|8|-1.113706|
|in|9|-0.864328|
|that|8|-0.841686|
|fracking|12|-0.831867|
|at|4|-0.721454|
|to|27|-0.576875|
|environmental|9|-0.514348|
|york|2|-0.513540|

### row_id=7878：sports → business

confidence=0.825577

原文：

i am often starkly aware that i'm participating in something truly amazing, yet at times incredibly challenging and humbling. after all, the participants in this fairy tale are still human.we cry i have lost count of how many times this environment has seemingly broken me. there have been days when the stress and repetitive failure has overpowered my ability to enjoy playing and stripped my motivation. but in those times i am surrounded by some of my best friends and people who find ways to support me and hoist me back up when i can't do it myself. if only i had a dollar for every time whitney engen has seen me break down and has provided a voice of reason. or there's heather o'reilly, who has encouraged me and made me feel valuable even when i couldn't see my own value. a kind word or supportive comment at training from carli lloyd reminded me that i'm not crazy when i think that i can achieve what i'm after, but it feels like i'm fighting an uphill battle . there is no level of success that eradicates moments of doubt, disappointment and despair. but there are no people i'd rather be around in those moments than these.we laugh in the soccer world, there is no moment too serious not to find some humor. whether it's a vine video that sydney leroux shows at dinner, lauren holiday (nee cheney) making fun of her defensive abilities in a video session, or someone goofing around with stephanie cox's baby daughter, the sound of laughter prevails in training camp . although we often roll our eyes at his sense of humor, coach tom sermanni likes to make light of things and even jokes with us about mistakes in training or games (which sometimes makes us cringe before we realize we are allowed to take a breath and relax. laughter is about survival. it brings joy to an otherwise tense and stressful environment. there is nothing funny about this group's goals and ambition, but we certainly don't take ourselves too seriously.we love when you care so deeply about what you do, and fully invest in it, you leave yourself exposed. for this reason, many of us have formed extremely tight bonds with one another. we have seen each other play and develop over the years. we have witnessed one another's ups and downs, seen each other get engaged, married and have children. we live together for weeks of intense training and talk about our hopes, fears, dreams and spiritual beliefs. for these reasons, we share a love that is like no other bond we will share in our lives. my teammates have seen me naked — in the figurative sense, not just in the shower — and accept me for who i am. and i love and respect them for that.we compete competitive by nature is an understatement. this is the kind of environment where a player's day is made or broken by a small-sided game in training; people slide during technical drills to try to make it work properly or save a stray pass; and card games in our spare time turn into fierce battles and weeklong arguments. everyone here wants to be the best, and everyone is really good at what they do. what i've realized is the best way to compete in this environment is with myself. this is the hardest working, most talented group of women i think i will ever encounter. we each bring a set of qualities to the table that is unique, and we must mold it to fit within the framework of the team. my job, and all i can control, is to make my skill set as potent and effective as i possibly can. so while we scrap and fight to win in anything and everything possible, my real competition exists internally.those of us fortunate to don the u.s. crest are privy to an environment like no other. this group fosters greatness, but simultaneously maintains a tough and grueling blue-collar mentality. the success is composed of individual efforts, yet the feeling of cooperative momentum is overwhelming. competing within the team is fierce, but fosters some of the closest bonds that life can offer. these paradoxes drive a level of success that is unparalleled in almost any field. at the end of the day, we play for our country, but we cry, laugh, love and compete for one another.yael averbuch, a native of montclair, n.j., has played professionally most recently in sweden.


最大贡献词（偏向预测类）：

|词|特征值|贡献|
|---|---|---|
|of|22|+2.848458|
|that|10|+2.480461|
|is|18|+1.737430|
|me|9|+1.695412|
|about|5|+1.512909|
|are|4|+1.307557|
|my|8|+1.228591|
|and|31|+0.945045|
|people|3|+0.913406|
|or|6|+0.894901|


最小贡献词（偏向真实类）：

|词|特征值|贡献|
|---|---|---|
|for|8|-1.432920|
|team|2|-1.344849|
|has|6|-1.339044|
|with|4|-1.061953|
|the|21|-1.017854|
|there|6|-0.894913|
|games|2|-0.884333|
|play|2|-0.730876|
|at|6|-0.699668|
|game|1|-0.646596|
