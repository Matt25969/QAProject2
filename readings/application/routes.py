from flask import render_template, redirect, url_for
from application import app
from application.models import readings
import requests

########FOR DEMO ONLY#########
@app.route("/", methods= ["GET", "POST"])
def reading():
    crystal=requests.get("http://crystals:5001").text
    card=requests.get("http://cards:5002").text
    reading= "Sorry about that...We are doing some updates.Just google it!"
    return reading

'''

@app.route("/", methods= ["GET", "POST"])
def reading():
    crystal=requests.get("http://crystals:5001").text
    card=requests.get("http://cards:5002").text
    
    if (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Fool":
        reading = "Immaturity, sincerity, the natural man, a free spirit. One who naturally knows his will and is worry free. A dreamer, careless and disinterested in practical matters. Travel."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Fool": 
        reading = "Reversed Meaning: Folly, failure, madness. Hindered travel!"
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Magician":
        reading = "Will, creativeness, adroitness, mastery, elasticity, autonomy, eloquence, craft, cunning. May imply a new beginning. The Magus is an autonomous person that knows where he is going and how to achieve its ends."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Magician":
        reading = "Reversed Meaning:Indecision, weak will, ineptitude, dilettante. Deceitfulness, trickery."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The High Priestess":
        reading = "Hidden influence. Silence, patience, equilibrium. Slow but firm. Pondered decision. Advice, tuition, possibly given by a woman. Psychic ability. The manifestation of the eternal feminine in a spiritual way."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The High Priestess":
        reading = "Reversed Meaning:Deceptive, secret, or sly manner. Lazyness, intolerance. Delays. False ideas, moodiness, doubt, superficiality."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Empress":
        reading = "Understanding, charm, kindness, beauty, pleasure, success, safety, trust. Nurturing, positive development."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Empress":
        reading = "Reversed Meaning:False appearance, vanity, disdain, frivolity. Sterility. Delays. Careless spending"
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Emperor":
        reading = " Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Emperor":
        reading = "Reversed Meaning: Loss of control. Emotional immaturity and bondage to parents. Possibility of being defrauded of one's inheritance. Ill-temper. Stubbornness. Fall. Loss of wealth. Megalomaniac."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Hierophant":
        reading = "Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart. The card that represents you, in the form of your own, truest voice, your own inner-self. Dogma. Can be lawyers."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Hierophant":
        reading = "Reversed Meaning:Tendency to over criticize or being unduly concerned with the morals of others. Incapable of dealing efficiently with practical matters, especially finances. Unconventionality, illogical, superstitious, unable to behave coherently."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Lovers":
        reading = "Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Lovers":
        reading = "Reversed Meaning:Disorder, failure, danger of a broken relationship or a wrong choice, quarrels, infidelity. Emotional instability. Dangerous temptation."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Chariot":
        reading = "Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Chariot":
        reading = "Reversed Meaning:Generalized disorder. Illness. Dangerous restlessness. Danger of a violent accidente."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "Strength":
        reading = "Sublimation or regulation of the passions and lower instincts. Power, energy, great love. Spirit ruling over matter. Action, courage. Success. Powerful will and great physical strength. The inner strength to tame the lust."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "Strength":
        reading = "Reversed Meaning:Discord, ruin, stubbornness, abuse of power. Weakness."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Hermit":
        reading = "Prudence, wisdom, patience, silence, spiritual advance, divine inspiration, circumspection, retirement from participation in current events, solitude. Pilgrimage. Quest for wisdom. Could be a teacher. A period of spiritual and intellectual personal development."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Hermit":
        reading = "Reversed Meaning: Immaturity, viciousness, darkness, stubbornness, deception, betrayal, too much or insufficient prudence. Misanthrope, misogyny, celibacy, excessively shy person. Hidden enemies."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Wheel of Fortune":
        reading = "Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Wheel of Fortune":
        reading = "Reversed Meaning:Retarded progress. Delays, setbacks."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "Justice":
        reading = "Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. Justice, balance, adjustment. In order to keep things balanced certain things must be sacrificed.. May refer to law matters, trials, marriages, divorces, etc. Integrity, moderation."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "Justice":
        reading = "Reversed Meaning:Fanaticism, injustice, inequality, legal complications. Harsh judgment. Insecurity, imbalance."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Hanged Man":
        reading = "Fortitude, wisdom. Self-imposed limitations. Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Hanged Man":
        reading = "Reversed Meaning:Arrogance, egotism, resistance to spiritual influences. Absorption in physical matters. Wasted effort. False prophecy. Failure."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "Death":
        reading = "Complete transformation. Death and rebirth. The end of something. Evolution from one state to another."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "Death":
        reading = "Reversed Meaning:Stagnation, death, petrification. Incurable ill person. Broken marriage"
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "Temperance":
        reading = "Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint. Patience, bringing together two opposites carefully blending them. Good marriage. Working in harmony with others, good management. Something is brewing. Great talent and creative involvement. Striving for Transcendence through works. Alchemy. The union of opposites refined by the fire of the Will."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "Temperance":
        reading = "Reversed Meaning:Disorder, conflict, unfortunate combinations, quarrels. Possibility of shipwreck."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Devil":
        reading = "Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Devil":
        reading = "Reversed Meaning: Harmful, fate, wrong use of force, weakness, blindness, disorder. Malefic effects. The pathetic human condition of choosing illusion over truth."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Blasted Tower":
        reading = "Sudden changes without choice, collapse, escape from prison or bondages, accident. Plans will fall, intentions will break down. Finger of God. Bankruptcy. Sudden death."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Blasted Tower":
        reading = "Reversed Meaning:Complete confusion. The gain of freedom at great cost. False accusations, oppression."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Star":
        reading = "Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Star":
        reading = "Reversed Meaning:Arrogance, pessimism, stubbornness. Illness. Error of judgment"
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Moon":
        reading = "Intuition, threshold of an important change, arduous and obscure path, development of psychic powers."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Moon":
        reading = "Reversed Meaning: Unforeseen perils, secret foes, hallucination, self-deception, hysteria, disorientation. Blackmailer."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The Sun":
        reading = "Glory. Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The Sun":
        reading = "Reversed Meaning:Anoyances, disguise. Arrogance. Broken engagement or lost job."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "Judgement":
        reading = "Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment. Creative power and influence over family and career. Forgiveness. Awakening. Legal judgments, in one's favor."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "Judgement":
        reading = "Reversed Meaning:Spiritual vacillation, weakness, wrong judgment. Illness. Separation. Adverse legal judgment."
    elif (crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite") and  card == "The World":
        reading = "Success granted. Rewards. Travel, emigration, change of residence."
    elif (crystal== "Azurite" or crystal =="Tiger's Eye" or crystal == "Blue Lacee") and  card == "The World":
        reading = "Reversed Meaning:Hindrances, stagnation. Hard work to bring success."
    else:
        #in case i missed a card
        reading = "Sorry about that...Please refresh!"
    return reading
'''   
