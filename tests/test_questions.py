import mini_watson
ir = mini_watson.Watson("wiki", "index")

def test_question_1():
	response = ir.guess("The dominant paper in our nation's capital, it's among the top 10 U.S. papers in circulation")
	assert response == "The Washington Post"

def test_question_2():
	response = ir.guess("The practice of pre-authorizing presidential use of force dates to a 1955 resolution re: this island near mainland China")
	assert response == "Taiwan"

def test_question_3():
	response = ir.guess("Daniel Hertzberg & James B. Stewart of this paper shared a 1988 Pulitzer for their stories about insider trading")
	assert response == "The Wall Street Journal"

def test_question_4():
	response = ir.guess("Song that says, \"you make me smile with my heart; your looks are laughable, unphotographable\"")
	assert response == "My Funny Valentine"

def test_question_5():
	response = ir.guess("In 2011 bell ringers for this charity started accepting digital donations to its red kettle")
	assert response == "The Salvation Army|Salvation Army"

def test_question_6():
	response = ir.guess("The Naples Museum of Art")
	assert response == "Florida"

def test_question_7():
	response = ir.guess("This Italian painter depicted the \"Adoration of the Golden Calf\"")
	assert response == "Tintoretto"

def test_question_8():
	response = ir.guess("This woman who won consecutive heptathlons at the Olympics went to UCLA on a basketball scholarship")
	assert response == "Jackie Joyner-Kersee"

def test_question_9():
	response = ir.guess("Originally this club's emblem was a wagon wheel; now it's a gearwheel with 24 cogs & 6 spokes")
	assert response == "Rotary International"

def test_question_10():
	response = ir.guess("Several bridges, including El Tahrir, cross the Nile in this capital")
	assert response == "Cairo"

def test_question_11():
	response = ir.guess("After the fall of France in 1940, this general told his country, \"France has lost a battle. But France has not lost the war\"")
	assert response == "Charles de Gaulle|de Gaulle"

def test_question_12():
	response = ir.guess("The Taft Museum of Art")
	assert response == "Ohio"

def test_question_13():
	response = ir.guess("The mast from the USS Maine is part of the memorial to the ship & crew at this national cemetery")
	assert response == "Arlington National Cemetery|Arlington Cemetery"

def test_question_14():
	response = ir.guess("In 2009: Joker on film")
	assert response == "Heath Ledger"

def test_question_15():
	response = ir.guess("It was the peninsula fought over in the peninsular war of 1808 to 1814")
	assert response == "Iberia|Iberian Peninsula"

def test_question_16():
	response = ir.guess("In 1980 China founded a center for these cute creatures in its bamboo-rich Wolong Nature Preserve")
	assert response == "Panda|Giant panda"

def test_question_17():
	response = ir.guess("1988: \"Father Figure\"")
	assert response == "George Michael"

def test_question_18():
	response = ir.guess("In an essay defending this 2011 film, Myrlie Evers-Williams said, \"My mother was\" this film \"& so was her mother\"")
	assert response == "The Help"

def test_question_19():
	response = ir.guess("Father Michael McGivney founded this fraternal society for Catholic laymen in 1882")
	assert response == "Knights of Columbus"

def test_question_20():
	response = ir.guess("Early projects of the WWF, this organization, included work with the bald eagle & the red wolf")
	assert response == "World Wide Fund|World Wide Fund for Nature"

def test_question_21():
	response = ir.guess("Indonesia's largest lizard, it's protected from poachers, though we wish it could breathe fire to do the job itself")
	assert response == "Komodo dragon"

def test_question_22():
	response = ir.guess("Nov. 28, 1929! This man & his chief pilot Bernt Balchen fly to South Pole! Yowza! You'll be an admirable admiral, sir!")
	assert response == "Richard Byrd|Richard E. Byrd"

def test_question_23():
	response = ir.guess("On May 5, 1878 Alice Chambers was the last person buried in this Dodge City, Kansas cemetery")
	assert response == "Boot Hill"

def test_question_24():
	response = ir.guess("The Royal Palace grounds feature a statue of King Norodom, who in the late 1800s was compelled to first put his country under the control of this European power; of course, it was sculpted in that country")
	assert response == "France"

def test_question_25():
	response = ir.guess("In the 400s B.C. this Chinese philosopher went into exile for 12 years")
	assert response == "Confucius"

def test_question_26():
	response = ir.guess("Bessie Coleman, the first black woman licensed as a pilot, landed a street named in her honor at this Chicago airport")
	assert response == "O'Hare|O'Hare International Airport"

def test_question_27():
	response = ir.guess("The Ammonites held sway in this Mideast country in the 1200s B.C. & the capital is named for them")
	assert response == "Jordan"

def test_question_28():
	response = ir.guess("\"The Sum of All Fears\"; he also won a screenwriting Oscar for \"Good Will Hunting\"")
	assert response == "Ben Affleck"

def test_question_29():
	response = ir.guess("One of the N.Y. Times' headlines on this landmark 1973 Supreme Court decision was \"Cardinals shocked\"")
	assert response == "Roe v. Wade"

def test_question_30():
	response = ir.guess("France's Philip IV--known as \"The Fair\"--had Jacques De Molay, the last Grand Master of this order, burned in 1314")
	assert response == "Knights Templar"

def test_question_31():
	response = ir.guess("The Georgia O'Keeffe Museum")
	assert response == "New Mexico"

def test_question_32():
	response = ir.guess("The name of this largest Moroccan city combines 2 Spanish words")
	assert response == "Casablanca"

def test_question_33():
	response = ir.guess("Jell-O")
	assert response == "Kraft Foods"

def test_question_34():
	response = ir.guess("2011: Chicago mayor Tom Kane")
	assert response == "Kelsey Grammer"

def test_question_35():
	response = ir.guess("Title residence of Otter, Flounder, Pinto & Bluto in a 1978 comedy")
	assert response == "Animal House"

def test_question_36():
	response = ir.guess("Neurobiologist Amy Farrah Fowler on \"The Big Bang Theory\", in real life she has a Ph.D. in neuroscience from UCLA")
	assert response == "Mayim Bialik"

def test_question_37():
	response = ir.guess("In \"The Deadlocked Election of 1800\", James R. Sharp outlines the fall of this dueling vice president")
	assert response == "Aaron Burr"

def test_question_38():
	response = ir.guess("He served in the KGB before becoming president & then prime minister of Russia")
	assert response == "Vladimir Putin|Putin"

def test_question_39():
	response = ir.guess("When asked to describe herself, she says first & foremost, she is Malia & Sasha's mom")
	assert response == "Michelle Obama"

def test_question_40():
	response = ir.guess("She wrote, \"My candle burns at both ends... but, ah, my foes, and oh, my friends--it gives a lovely light\"")
	assert response == "Edna St. Vincent Millay"

def test_question_41():
	response = ir.guess("In this Finnish city, the Lutheran Cathedral, also known as Tuomiokirkko")
	assert response == "Helsinki"

def test_question_42():
	response = ir.guess("Milton Bradley games")
	assert response == "Hasbro"

def test_question_43():
	response = ir.guess("The Kentucky & Virginia resolutions were passed to protest these controversial 1798 acts of Congress")
	assert response == "The Alien and Sedition Acts"

def test_question_44():
	response = ir.guess("1983: \"Beat It\"")
	assert response == "Michael Jackson"

def test_question_45():
	response = ir.guess("In 2009: Sookie Stackhouse")
	assert response == "Anna Paquin"

def test_question_46():
	response = ir.guess("This member of the Nixon & Ford cabinets was born in Furth, Germany in 1923")
	assert response == "Henry Kissinger"

def test_question_47():
	response = ir.guess("The High Kirk of St. Giles, where John Knox was minister")
	assert response == "Edinburgh"

def test_question_48():
	response = ir.guess("For the brief time he attended, he was a rebel with a cause, even landing a lead role in a 1950 stage production")
	assert response == "James Dean"

def test_question_49():
	response = ir.guess("Fisher-Price toys")
	assert response == "Mattel"

def test_question_50():
	response = ir.guess("In a 1959 American kitchen exhibit in Moscow, he told Khrushchev, \"In America, we like to make life easier for women\"")
	assert response == "Richard Nixon|Nixon"

def test_question_51():
	response = ir.guess("One of his \"Tales of a Wayside Inn\" begins, \"Listen, my children, and you shall hear of the midnight ride of Paul Revere\"")
	assert response == "Henry Wadsworth Longfellow"

def test_question_52():
	response = ir.guess("This bestseller about problems on the McCain-Palin ticket became an HBO movie with Julianne Moore")
	assert response == "Game Change"

def test_question_53():
	response = ir.guess("A 2-part episode of \"JAG\" introduced this Mark Harmon drama")
	assert response == "NCIS"

def test_question_54():
	response = ir.guess("This port is the southernmost of South Africa's 3 capitals")
	assert response == "Cape Town"

def test_question_55():
	response = ir.guess("Keats was quoting this Edmund Spenser poem when he told Shelley to \"'load every rift' of your subject with ore\"")
	assert response == "The Faerie Queene"

def test_question_56():
	response = ir.guess("In an 1819 letter Keats wrote that this lord & poet \"cuts a figure, but he is not figurative\"")
	assert response == "Lord Byron"

def test_question_57():
	response = ir.guess("This clear Greek liqueur is quite potent, so it's usually mixed with water, which turns it white & cloudy")
	assert response == "Ouzo"

def test_question_58():
	response = ir.guess("Feb. 1, National Freedom Day, is the date in 1865 when a resolution sent the states an amendment ending this")
	assert response == "Slavery|Slavery in the United States"

def test_question_59():
	response = ir.guess("This person is the queen's representative in Canada; currently the office is held by David Johnston")
	assert response == "Governor General of Canada"

def test_question_60():
	response = ir.guess("He earned the \"fifth Beatle\" nickname by producing all of the Beatles' albums")
	assert response == "George Martin"

def test_question_61():
	response = ir.guess("Early in their careers, Mark Twain & Bret Harte wrote pieces for this California city's Chronicle")
	assert response == "San Francisco"

def test_question_62():
	response = ir.guess("Large specimens of this marsupial can leap over barriers 6 feet high")
	assert response == "Kangaroo"

def test_question_63():
	response = ir.guess("Because it's cured & stored in brine, this crumbly white cheese made from sheep's milk is often referred to as pickled cheese")
	assert response == "Feta"

def test_question_64():
	response = ir.guess("1927! Gene Tunney takes a long count in the squared circle but rises to defeat this \"Manassa Mauler\"! Howzabout that!")
	assert response == "Jack Dempsey"

def test_question_65():
	response = ir.guess("Italian for \"leader\", it was especially applied to Benito Mussolini")
	assert response == "Duce"

def test_question_66():
	response = ir.guess("The Kalamazoo Institute of Arts")
	assert response == "Michigan"

def test_question_67():
	response = ir.guess("The Sun Valley Center for the Arts")
	assert response == "Idaho"

def test_question_68():
	response = ir.guess("You can't mention this shortstop without mentioning his double-play associates Evers & Chance")
	assert response == "Joe Tinker"

def test_question_69():
	response = ir.guess("In 1840 Horace Greeley began publishing \"The Log Cabin\", a weekly campaign paper in support of this Whig candidate")
	assert response == "William Henry Harrison"

def test_question_70():
	response = ir.guess("Pierre Cauchon, Bishop of Beauvais, presided over the trial of this woman who went up in smoke May 30, 1431")
	assert response == "Joan of Arc|Jeanne d'Arc"

def test_question_71():
	response = ir.guess("This Wisconsin city claims to have built the USA's only granite dome")
	assert response == "Madison"

def test_question_72():
	response = ir.guess("This Georgia paper is known as the AJC for short")
	assert response == "The Atlanta Journal-Constitution"

def test_question_73():
	response = ir.guess("Wooden 2-story verandas in this Liberian capital are an architectural link to the U.S. south")
	assert response == "Monrovia"

def test_question_74():
	response = ir.guess("This New Orleans venue reopened Sept. 25, 2006")
	assert response == "Mercedes-Benz Superdome|The Superdome"

def test_question_75():
	response = ir.guess("\"The Hunt for Red October\"; he went more comedic as Jack Donaghy on \"30 Rock\"")
	assert response == "Alec Baldwin"

def test_question_76():
	response = ir.guess("Rita Dove titled a collection of poems \"On the Bus with\" this woman")
	assert response == "Rosa Parks"

def test_question_77():
	response = ir.guess("\"Patriot Games\"; he's had other iconic roles, in space & underground")
	assert response == "Harrison Ford"

def test_question_78():
	response = ir.guess("This sacred structure dates from the late 600's A.D.")
	assert response == "Dome of the Rock"

def test_question_79():
	response = ir.guess("1988: \"Man In The Mirror\"")
	assert response == "Michael Jackson"

def test_question_80():
	response = ir.guess("Matthias Church, or Matyas Templom, where Franz Joseph was crowned in 1867")
	assert response == "Budapest"

def test_question_81():
	response = ir.guess("Attending UCLA in the '60s, he was no \"Meathead\", he just played one later on television")
	assert response == "Rob Reiner"

def test_question_82():
	response = ir.guess("Kinch, Carter & LeBeau were all residents of Stalag 13 on this TV show")
	assert response == "Hogan's Heroes"

def test_question_83():
	response = ir.guess("News flash! This less-than-yappy pappy is sixth veep to be nation's top dog after chief takes deep sleep!")
	assert response == "Calvin Coolidge"

def test_question_84():
	response = ir.guess("In 2001: The president of the United States on television")
	assert response == "Martin Sheen"

def test_question_85():
	response = ir.guess("1989: \"Miss You Much\"")
	assert response == "Janet Jackson"

def test_question_86():
	response = ir.guess("1922: It's the end of an empire! This empire, in fact! After 600 years, it's goodbye, this, hello, Turkish Republic!")
	assert response == "Ottoman Empire"

def test_question_87():
	response = ir.guess("Crest toothpaste")
	assert response == "Procter & Gamble"

def test_question_88():
	response = ir.guess("In 1888 this Chancellor told the Reichstag, \"we Germans fear God, but nothing else in the world\"")
	assert response == "Otto von Bismarck|Von Bismarck"

def test_question_89():
	response = ir.guess("In 1787 he signed his first published poem \"Axiologus\"; axio- is from the Greek for \"worth\"")
	assert response == "William Wordsworth"

def test_question_90():
	response = ir.guess("Not to be confused with karma, krama is a popular accessory sold in cambodia; the word means \"scarf\" in this national language of Cambodia")
	assert response == "Khmer language"

def test_question_91():
	response = ir.guess("Phnom Penh's notorious gridlock is circumvented by the nimble tuk-tuk, a motorized taxi that's also known as an auto this, a similar Asian conveyance.")
	assert response == "Rickshaw"

def test_question_92():
	response = ir.guess("1980: \"Rock With You\"")
	assert response == "Michael Jackson"

def test_question_93():
	response = ir.guess("The Pulitzer-winning \"The Making of the President 1960\" covered this man's successful presidential campaign")
	assert response == "JFK|John F. Kennedy"

def test_question_94():
	response = ir.guess("In 1843 Isaac Dittenhoefer became the first pres. of this Jewish club whose name means \"children of the covenant\"")
	assert response == "B'nai B'rith"

def test_question_95():
	response = ir.guess("Don Knotts took over from Norman Fell as the resident landlord on this sitcom")
	assert response == "Three's Company"

def test_question_96():
	response = ir.guess("U.N. Res. 242 supports \"secure and recognized boundaries\" for Israel & neighbors following this June 1967 war")
	assert response == "The Six Day War"

def test_question_97():
	response = ir.guess("This blonde beauty who reprised her role as Amanda on the new \"Melrose Place\" was a psychology major")
	assert response == "Heather Locklear"

def test_question_98():
	response = ir.guess("The name of this dish of marinated lamb, skewered & grilled, comes from the Greek for \"skewer\" & also starts with \"s\"")
	assert response == "Souvlaki"

def test_question_99():
	response = ir.guess("Post-it notes")
	assert response == "3M"

def test_question_100():
	response = ir.guess("In 2010: As Sherlock Holmes on film")
	assert response == "Robert Downey, Jr."
