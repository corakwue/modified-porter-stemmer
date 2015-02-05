# modified-porter-stemmer
NTLK Porter Stemmer with modifications to improve performance.

Also attached if quick script to validate performance. 

Example performance:

| Word/Stemmer     | Lancaster    | *Modified-Porter*   | WordNet-Lemma    | Porter         | Snowball-EN    |
|------------------|--------------|-------------------|------------------|----------------|----------------|
| elaborates       | elab         | elaborate         | elaborates       | elabor         | elabor         |
| activate         | act          | activate          | activate         | activ          | activ          |
| critically       | crit         | critic            | critically       | critic         | critic         |
| substituting     | substitut    | substitute        | substituting     | substitut      | substitut      |
| learning         | learn        | learn             | learning         | learn          | learn          |
| educating        | educ         | educate           | educating        | educ           | educ           |
| creation         | cre          | creation          | creation         | creation       | creation       |
| braille          | brail        | braille           | braille          | braill         | braill         |
| security         | sec          | security          | security         | secur          | secur          |
| business         | busy         | business          | business         | busi           | busi           |
| tenderness       | tend         | tendere           | tenderness       | tender         | tender         |
| tabulate         | tab          | tabulate          | tabulate         | tabul          | tabul          |
| connections      | connect      | connect           | connection       | connect        | connect        |
| relativity       | rel          | rel               | relativity       | rel            | relat          |
| geography        | geograph     | geography         | geography        | geographi      | geographi      |
| unseparable      | unsep        | unsepare          | unseparable      | unsepar        | unsepar        |
| beauty           | beauty       | beauti            | beauty           | beauti         | beauti         |
| beautiful        | beauty       | beauti            | beautiful        | beauti         | beauti         |
| ability          | abl          | able              | ability          | abil           | abil           |
| interpilastering | interpilast  | interpilastere    | interpilastering | interpilast    | interpilast    |
| interplanetary   | interplanet  | interplanet       | interplanetary   | interplanetari | interplanetari |
| gluttingly       | glut         | glut              | gluttingly       | gluttingli     | glut           |
| especially       | espec        | especi            | especially       | especi         | especi         |
| psychobiology    | psychobiolog | psychobiology     | psychobiology    | psychobiolog   | psychobiolog   |
| magical          | mag          | magic             | magical          | magic          | magic          |
| magically        | mag          | magic             | magically        | magic          | magic          |
| adulatory        | ad           | adulate           | adulatory        | adulatori      | adulatori      |
| mandatory        | mand         | mandate           | mandatory        | mandatori      | mandatori      |
| microchemistry   | microchem    | microchemistry    | microchemistry   | microchemistri | microchemistri |
| scorningly       | scorn        | scorn             | scorningly       | scorningli     | scorn          |
| excystate        | excyst       | excystate         | excystate        | excyst         | excyst         |
| execrable        | execr        | execre            | execrable        | execr          | execr          |
| statued          | statu        | statue            | statued          | statu          | statu          |
| statuary         | statu        | statue            | statuary         | statuari       | statuari       |
| sparringly       | spar         | spare             | sparringly       | sparringli     | spar           |