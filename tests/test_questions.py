import mini_watson
from mini_watson import Watson
ir = mini_watson.Watson("wiki", "index")

def test_question_1():
	response = ir.run_query("NEWSPAPERS, The dominant paper in our nation's capital, it's among the top 10 U.S. papers in circulation")
	print(Watson.pretty(response))
	assert response[0]['title'] == "The Washington Post"

def test_question_2():
	response = ir.run_query("OLD YEAR'S RESOLUTIONS, The practice of pre-authorizing presidential use of force dates to a 1955 resolution re: this island near mainland China")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Taiwan"

def test_question_3():
	response = ir.run_query("NEWSPAPERS, Daniel Hertzberg & James B. Stewart of this paper shared a 1988 Pulitzer for their stories about insider trading")
	print(Watson.pretty(response))
	assert response[0]['title'] == "The Wall Street Journal"

def test_question_4():
	response = ir.run_query("BROADWAY LYRICS, Song that says, \"you make me smile with my heart; your looks are laughable, unphotographable\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "My Funny Valentine"

def test_question_5():
	response = ir.run_query("POTPOURRI, In 2011 bell ringers for this charity started accepting digital donations to its red kettle")
	print(Watson.pretty(response))
	assert response[0]['title'] == "The Salvation Army|Salvation Army"

def test_question_6():
	response = ir.run_query("STATE OF THE ART MUSEUM (Alex: We'll give you the museum. You give us the state.), The Naples Museum of Art")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Florida"

def test_question_7():
	response = ir.run_query("\"TIN\" MEN, This Italian painter depicted the \"Adoration of the Golden Calf\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Tintoretto"

def test_question_8():
	response = ir.run_query("UCLA CELEBRITY ALUMNI, This woman who won consecutive heptathlons at the Olympics went to UCLA on a basketball scholarship")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Jackie Joyner-Kersee"

def test_question_9():
	response = ir.run_query("SERVICE ORGANIZATIONS, Originally this club's emblem was a wagon wheel; now it's a gearwheel with 24 cogs & 6 spokes")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Rotary International"

def test_question_10():
	response = ir.run_query("AFRICAN CITIES, Several bridges, including El Tahrir, cross the Nile in this capital")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Cairo"

def test_question_11():
	response = ir.run_query("HISTORICAL QUOTES, After the fall of France in 1940, this general told his country, \"France has lost a battle. But France has not lost the war\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Charles de Gaulle|de Gaulle"

def test_question_12():
	response = ir.run_query("STATE OF THE ART MUSEUM (Alex: We'll give you the museum. You give us the state.), The Taft Museum of Art")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Ohio"

def test_question_13():
	response = ir.run_query("CEMETERIES, The mast from the USS Maine is part of the memorial to the ship & crew at this national cemetery")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Arlington National Cemetery|Arlington Cemetery"

def test_question_14():
	response = ir.run_query("GOLDEN GLOBE WINNERS, In 2009: Joker on film")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Heath Ledger"

def test_question_15():
	response = ir.run_query("HISTORICAL HODGEPODGE, It was the peninsula fought over in the peninsular war of 1808 to 1814")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Iberia|Iberian Peninsula"

def test_question_16():
	response = ir.run_query("CONSERVATION, In 1980 China founded a center for these cute creatures in its bamboo-rich Wolong Nature Preserve")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Panda|Giant panda"

def test_question_17():
	response = ir.run_query("'80s NO.1 HITMAKERS, 1988: \"Father Figure\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "George Michael"

def test_question_18():
	response = ir.run_query("AFRICAN-AMERICAN WOMEN, In an essay defending this 2011 film, Myrlie Evers-Williams said, \"My mother was\" this film \"& so was her mother\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "The Help"

def test_question_19():
	response = ir.run_query("SERVICE ORGANIZATIONS, Father Michael McGivney founded this fraternal society for Catholic laymen in 1882")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Knights of Columbus"

def test_question_20():
	response = ir.run_query("CONSERVATION, Early projects of the WWF, this organization, included work with the bald eagle & the red wolf")
	print(Watson.pretty(response))
	assert response[0]['title'] == "World Wide Fund|World Wide Fund for Nature"

def test_question_21():
	response = ir.run_query("CONSERVATION, Indonesia's largest lizard, it's protected from poachers, though we wish it could breathe fire to do the job itself")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Komodo dragon"

def test_question_22():
	response = ir.run_query("1920s NEWS FLASH!, Nov. 28, 1929! This man & his chief pilot Bernt Balchen fly to South Pole! Yowza! You'll be an admirable admiral, sir!")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Richard Byrd|Richard E. Byrd"

def test_question_23():
	response = ir.run_query("CEMETERIES, On May 5, 1878 Alice Chambers was the last person buried in this Dodge City, Kansas cemetery")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Boot Hill"

def test_question_24():
	response = ir.run_query("CAMBODIAN HISTORY & CULTURE, The Royal Palace grounds feature a statue of King Norodom, who in the late 1800s was compelled to first put his country under the control of this European power; of course, it was sculpted in that country")
	print(Watson.pretty(response))
	assert response[0]['title'] == "France"

def test_question_25():
	response = ir.run_query("HISTORICAL HODGEPODGE, In the 400s B.C. this Chinese philosopher went into exile for 12 years")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Confucius"

def test_question_26():
	response = ir.run_query("AFRICAN-AMERICAN WOMEN, Bessie Coleman, the first black woman licensed as a pilot, landed a street named in her honor at this Chicago airport")
	print(Watson.pretty(response))
	assert response[0]['title'] == "O'Hare|O'Hare International Airport"

def test_question_27():
	response = ir.run_query("HISTORICAL HODGEPODGE, The Ammonites held sway in this Mideast country in the 1200s B.C. & the capital is named for them")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Jordan"

def test_question_28():
	response = ir.run_query("HE PLAYED A GUY NAMED JACK RYAN IN..., \"The Sum of All Fears\"; he also won a screenwriting Oscar for \"Good Will Hunting\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Ben Affleck"

def test_question_29():
	response = ir.run_query("POTPOURRI, One of the N.Y. Times' headlines on this landmark 1973 Supreme Court decision was \"Cardinals shocked\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Roe v. Wade"

def test_question_30():
	response = ir.run_query("I'M BURNIN' FOR YOU, France's Philip IV--known as \"The Fair\"--had Jacques De Molay, the last Grand Master of this order, burned in 1314")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Knights Templar"

def test_question_31():
	response = ir.run_query("STATE OF THE ART MUSEUM (Alex: We'll give you the museum. You give us the state.), The Georgia O'Keeffe Museum")
	print(Watson.pretty(response))
	assert response[0]['title'] == "New Mexico"

def test_question_32():
	response = ir.run_query("AFRICAN CITIES, The name of this largest Moroccan city combines 2 Spanish words")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Casablanca"

def test_question_33():
	response = ir.run_query("NAME THE PARENT COMPANY, Jell-O")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Kraft Foods"

def test_question_34():
	response = ir.run_query("GOLDEN GLOBE WINNERS, 2011: Chicago mayor Tom Kane")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Kelsey Grammer"

def test_question_35():
	response = ir.run_query("THE RESIDENTS, Title residence of Otter, Flounder, Pinto & Bluto in a 1978 comedy")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Animal House"

def test_question_36():
	response = ir.run_query("UCLA CELEBRITY ALUMNI, Neurobiologist Amy Farrah Fowler on \"The Big Bang Theory\", in real life she has a Ph.D. in neuroscience from UCLA")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Mayim Bialik"

def test_question_37():
	response = ir.run_query("NOTES FROM THE CAMPAIGN TRAIL, In \"The Deadlocked Election of 1800\", James R. Sharp outlines the fall of this dueling vice president")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Aaron Burr"

def test_question_38():
	response = ir.run_query("\"TIN\" MEN, He served in the KGB before becoming president & then prime minister of Russia")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Vladimir Putin|Putin"

def test_question_39():
	response = ir.run_query("AFRICAN-AMERICAN WOMEN, When asked to describe herself, she says first & foremost, she is Malia & Sasha's mom")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Michelle Obama"

def test_question_40():
	response = ir.run_query("POETS & POETRY, She wrote, \"My candle burns at both ends... but, ah, my foes, and oh, my friends--it gives a lovely light\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Edna St. Vincent Millay"

def test_question_41():
	response = ir.run_query("CAPITAL CITY CHURCHES (Alex: We'll give you the church. You tell us the capital city in which it is located.), In this Finnish city, the Lutheran Cathedral, also known as Tuomiokirkko")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Helsinki"

def test_question_42():
	response = ir.run_query("NAME THE PARENT COMPANY, Milton Bradley games")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Hasbro"

def test_question_43():
	response = ir.run_query("OLD YEAR'S RESOLUTIONS, The Kentucky & Virginia resolutions were passed to protest these controversial 1798 acts of Congress")
	print(Watson.pretty(response))
	assert response[0]['title'] == "The Alien and Sedition Acts"

def test_question_44():
	response = ir.run_query("'80s NO.1 HITMAKERS, 1983: \"Beat It\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Michael Jackson"

def test_question_45():
	response = ir.run_query("GOLDEN GLOBE WINNERS, In 2009: Sookie Stackhouse")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Anna Paquin"

def test_question_46():
	response = ir.run_query("HISTORICAL HODGEPODGE, This member of the Nixon & Ford cabinets was born in Furth, Germany in 1923")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Henry Kissinger"

def test_question_47():
	response = ir.run_query("CAPITAL CITY CHURCHES (Alex: We'll give you the church. You tell us the capital city in which it is located.), The High Kirk of St. Giles, where John Knox was minister")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Edinburgh"

def test_question_48():
	response = ir.run_query("UCLA CELEBRITY ALUMNI, For the brief time he attended, he was a rebel with a cause, even landing a lead role in a 1950 stage production")
	print(Watson.pretty(response))
	assert response[0]['title'] == "James Dean"

def test_question_49():
	response = ir.run_query("NAME THE PARENT COMPANY, Fisher-Price toys")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Mattel"

def test_question_50():
	response = ir.run_query("HISTORICAL QUOTES, In a 1959 American kitchen exhibit in Moscow, he told Khrushchev, \"In America, we like to make life easier for women\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Richard Nixon|Nixon"

def test_question_51():
	response = ir.run_query("POETS & POETRY, One of his \"Tales of a Wayside Inn\" begins, \"Listen, my children, and you shall hear of the midnight ride of Paul Revere\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Henry Wadsworth Longfellow"

def test_question_52():
	response = ir.run_query("NOTES FROM THE CAMPAIGN TRAIL, This bestseller about problems on the McCain-Palin ticket became an HBO movie with Julianne Moore")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Game Change"

def test_question_53():
	response = ir.run_query("THAT 20-AUGHTS SHOW, A 2-part episode of \"JAG\" introduced this Mark Harmon drama")
	print(Watson.pretty(response))
	assert response[0]['title'] == "NCIS"

def test_question_54():
	response = ir.run_query("AFRICAN CITIES, This port is the southernmost of South Africa's 3 capitals")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Cape Town"

def test_question_55():
	response = ir.run_query("THE QUOTABLE KEATS, Keats was quoting this Edmund Spenser poem when he told Shelley to \"'load every rift' of your subject with ore\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "The Faerie Queene"

def test_question_56():
	response = ir.run_query("THE QUOTABLE KEATS, In an 1819 letter Keats wrote that this lord & poet \"cuts a figure, but he is not figurative\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Lord Byron"

def test_question_57():
	response = ir.run_query("GREEK FOOD & DRINK, This clear Greek liqueur is quite potent, so it's usually mixed with water, which turns it white & cloudy")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Ouzo"

def test_question_58():
	response = ir.run_query("OLD YEAR'S RESOLUTIONS, Feb. 1, National Freedom Day, is the date in 1865 when a resolution sent the states an amendment ending this")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Slavery|Slavery in the United States"

def test_question_59():
	response = ir.run_query("RANKS & TITLES, This person is the queen's representative in Canada; currently the office is held by David Johnston")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Governor General of Canada"

def test_question_60():
	response = ir.run_query("\"TIN\" MEN, He earned the \"fifth Beatle\" nickname by producing all of the Beatles' albums")
	print(Watson.pretty(response))
	assert response[0]['title'] == "George Martin"

def test_question_61():
	response = ir.run_query("NEWSPAPERS, Early in their careers, Mark Twain & Bret Harte wrote pieces for this California city's Chronicle")
	print(Watson.pretty(response))
	assert response[0]['title'] == "San Francisco"

def test_question_62():
	response = ir.run_query("POTPOURRI, Large specimens of this marsupial can leap over barriers 6 feet high")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Kangaroo"

def test_question_63():
	response = ir.run_query("GREEK FOOD & DRINK, Because it's cured & stored in brine, this crumbly white cheese made from sheep's milk is often referred to as pickled cheese")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Feta"

def test_question_64():
	response = ir.run_query("1920s NEWS FLASH!, 1927! Gene Tunney takes a long count in the squared circle but rises to defeat this \"Manassa Mauler\"! Howzabout that!")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Jack Dempsey"

def test_question_65():
	response = ir.run_query("RANKS & TITLES, Italian for \"leader\", it was especially applied to Benito Mussolini")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Duce"

def test_question_66():
	response = ir.run_query("STATE OF THE ART MUSEUM (Alex: We'll give you the museum. You give us the state.), The Kalamazoo Institute of Arts")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Michigan"

def test_question_67():
	response = ir.run_query("STATE OF THE ART MUSEUM (Alex: We'll give you the museum. You give us the state.), The Sun Valley Center for the Arts")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Idaho"

def test_question_68():
	response = ir.run_query("\"TIN\" MEN, You can't mention this shortstop without mentioning his double-play associates Evers & Chance")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Joe Tinker"

def test_question_69():
	response = ir.run_query("NEWSPAPERS, In 1840 Horace Greeley began publishing \"The Log Cabin\", a weekly campaign paper in support of this Whig candidate")
	print(Watson.pretty(response))
	assert response[0]['title'] == "William Henry Harrison"

def test_question_70():
	response = ir.run_query("I'M BURNIN' FOR YOU, Pierre Cauchon, Bishop of Beauvais, presided over the trial of this woman who went up in smoke May 30, 1431")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Joan of Arc|Jeanne d'Arc"

def test_question_71():
	response = ir.run_query("COMPLETE DOM-INATION(Alex: Not \"domination.\"), This Wisconsin city claims to have built the USA's only granite dome")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Madison"

def test_question_72():
	response = ir.run_query("NEWSPAPERS, This Georgia paper is known as the AJC for short")
	print(Watson.pretty(response))
	assert response[0]['title'] == "The Atlanta Journal-Constitution"

def test_question_73():
	response = ir.run_query("AFRICAN CITIES, Wooden 2-story verandas in this Liberian capital are an architectural link to the U.S. south")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Monrovia"

def test_question_74():
	response = ir.run_query("COMPLETE DOM-INATION(Alex: Not \"domination.\"), This New Orleans venue reopened Sept. 25, 2006")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Mercedes-Benz Superdome|The Superdome"

def test_question_75():
	response = ir.run_query("HE PLAYED A GUY NAMED JACK RYAN IN..., \"The Hunt for Red October\"; he went more comedic as Jack Donaghy on \"30 Rock\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Alec Baldwin"

def test_question_76():
	response = ir.run_query("AFRICAN-AMERICAN WOMEN, Rita Dove titled a collection of poems \"On the Bus with\" this woman")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Rosa Parks"

def test_question_77():
	response = ir.run_query("HE PLAYED A GUY NAMED JACK RYAN IN..., \"Patriot Games\"; he's had other iconic roles, in space & underground")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Harrison Ford"

def test_question_78():
	response = ir.run_query("COMPLETE DOM-INATION(Alex: Not \"domination.\"), This sacred structure dates from the late 600's A.D.")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Dome of the Rock"

def test_question_79():
	response = ir.run_query("'80s NO.1 HITMAKERS, 1988: \"Man In The Mirror\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Michael Jackson"

def test_question_80():
	response = ir.run_query("CAPITAL CITY CHURCHES (Alex: We'll give you the church. You tell us the capital city in which it is located.), Matthias Church, or Matyas Templom, where Franz Joseph was crowned in 1867")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Budapest"

def test_question_81():
	response = ir.run_query("UCLA CELEBRITY ALUMNI, Attending UCLA in the '60s, he was no \"Meathead\", he just played one later on television")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Rob Reiner"

def test_question_82():
	response = ir.run_query("THE RESIDENTS, Kinch, Carter & LeBeau were all residents of Stalag 13 on this TV show")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Hogan's Heroes"

def test_question_83():
	response = ir.run_query("1920s NEWS FLASH!, News flash! This less-than-yappy pappy is sixth veep to be nation's top dog after chief takes deep sleep!")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Calvin Coolidge"

def test_question_84():
	response = ir.run_query("GOLDEN GLOBE WINNERS, In 2001: The president of the United States on television")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Martin Sheen"

def test_question_85():
	response = ir.run_query("'80s NO.1 HITMAKERS, 1989: \"Miss You Much\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Janet Jackson"

def test_question_86():
	response = ir.run_query("1920s NEWS FLASH!, 1922: It's the end of an empire! This empire, in fact! After 600 years, it's goodbye, this, hello, Turkish Republic!")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Ottoman Empire"

def test_question_87():
	response = ir.run_query("NAME THE PARENT COMPANY, Crest toothpaste")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Procter & Gamble"

def test_question_88():
	response = ir.run_query("HISTORICAL QUOTES, In 1888 this Chancellor told the Reichstag, \"we Germans fear God, but nothing else in the world\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Otto von Bismarck|Von Bismarck"

def test_question_89():
	response = ir.run_query("POETS & POETRY, In 1787 he signed his first published poem \"Axiologus\"; axio- is from the Greek for \"worth\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "William Wordsworth"

def test_question_90():
	response = ir.run_query("CAMBODIAN HISTORY & CULTURE, Not to be confused with karma, krama is a popular accessory sold in cambodia; the word means \"scarf\" in this national language of Cambodia")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Khmer language"

def test_question_91():
	response = ir.run_query("CAMBODIAN HISTORY & CULTURE, Phnom Penh's notorious gridlock is circumvented by the nimble tuk-tuk, a motorized taxi that's also known as an auto this, a similar Asian conveyance.")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Rickshaw"

def test_question_92():
	response = ir.run_query("'80s NO.1 HITMAKERS, 1980: \"Rock With You\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Michael Jackson"

def test_question_93():
	response = ir.run_query("NOTES FROM THE CAMPAIGN TRAIL, The Pulitzer-winning \"The Making of the President 1960\" covered this man's successful presidential campaign")
	print(Watson.pretty(response))
	assert response[0]['title'] == "JFK|John F. Kennedy"

def test_question_94():
	response = ir.run_query("SERVICE ORGANIZATIONS, In 1843 Isaac Dittenhoefer became the first pres. of this Jewish club whose name means \"children of the covenant\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "B'nai B'rith"

def test_question_95():
	response = ir.run_query("THE RESIDENTS, Don Knotts took over from Norman Fell as the resident landlord on this sitcom")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Three's Company"

def test_question_96():
	response = ir.run_query("OLD YEAR'S RESOLUTIONS, U.N. Res. 242 supports \"secure and recognized boundaries\" for Israel & neighbors following this June 1967 war")
	print(Watson.pretty(response))
	assert response[0]['title'] == "The Six Day War"

def test_question_97():
	response = ir.run_query("UCLA CELEBRITY ALUMNI, This blonde beauty who reprised her role as Amanda on the new \"Melrose Place\" was a psychology major")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Heather Locklear"

def test_question_98():
	response = ir.run_query("GREEK FOOD & DRINK, The name of this dish of marinated lamb, skewered & grilled, comes from the Greek for \"skewer\" & also starts with \"s\"")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Souvlaki"

def test_question_99():
	response = ir.run_query("NAME THE PARENT COMPANY, Post-it notes")
	print(Watson.pretty(response))
	assert response[0]['title'] == "3M"

def test_question_100():
	response = ir.run_query("GOLDEN GLOBE WINNERS, In 2010: As Sherlock Holmes on film")
	print(Watson.pretty(response))
	assert response[0]['title'] == "Robert Downey, Jr."
