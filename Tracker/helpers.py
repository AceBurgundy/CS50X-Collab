
import os
from colorama import init
import secrets
from wtforms.validators import ValidationError
from flask import current_app, jsonify
from PIL import Image


def save_picture(form_picture):
    random_value = secrets.token_hex(8)
    file_name, file_extension = os.path.splitext(form_picture.filename)
    new_file_name = random_value + file_extension
    file_path = os.path.join(current_app.root_path,
                             'static/profile_pictures', new_file_name)

    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(file_path)

    return new_file_name


profanity = ['2 girls 1 cup', '2g1c', '4r5e', '5h1t', '5hit', 'a$$', 'a$$hole', 'a55', 'a55hole', 'a_s_s', 'acrotomophilia', 'ahole', 'alabama hot pocket', 'alaskan pipeline', 'anal', 'anal impaler', 'anal leakage', 'analprobe', 'anilingus', 'anus', 'apeshit', 'ar5e', 'arrse', 'arse', 'arsehole', 'ass', 'ass fuck', 'ass hole', 'ass-fucker', 'ass-hat', 'ass-jabber', 'ass-pirate', 'assbag', 'assbandit', 'assbang', 'assbanged', 'assbanger', 'assbangs', 'assbite', 'assclown', 'asscock', 'asscracker', 'asses', 'assface', 'assfaces', 'assfuck', 'assfucker', 'assfukka', 'assgoblin', 'assh0le', 'asshat', 'asshead', 'asshole', 'assholes', 'asshopper', 'assjacker', 'asslick', 'asslicker', 'assmonkey', 'assmunch', 'assmuncher', 'assnigger', 'asspirate', 'assshit', 'assshole', 'asssucker', 'asswad', 'asswhole', 'asswipe', 'auto erotic', 'autoerotic', 'axwound', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'babeland', 'baby batter', 'baby juice', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', 'ball sack', 'ball sucking', 'ballbag', 'balls', 'ballsack', 'bampot', 'bangbros', 'bareback', 'barely legal', 'barenaked', 'bastard', 'bastardo', 'bastinado', 'bbw', 'bdsm', 'beaner', 'beaners', 'beastial', 'beastiality', 'beatch', 'beaver cleaver', 'beaver lips', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'big black', 'big breasts', 'big knockers', 'big tits', 'bimbo', 'bimbos', 'birdlock', 'bitch', 'bitch tit', 'bitchass', 'bitched', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bitchtits', 'bitchy', 'black cock', 'blonde action', 'blonde on blonde action', 'bloody', 'bloody hell', 'blow job', 'blow your load', 'blowjob', 'blowjobs', 'blue waffle', 'blumpkin', 'boiolas', 'bollock', 'bollocks', 'bollok', 'bollox', 'bondage', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'bootee', 'bootie', 'booty call', 'breasts', 'breeder', 'brotherfucker', 'brown showers', 'brunette action', 'buceta', 'bugger', 'bukkake', 'bull shit', 'bulldyke', 'bullet vibe', 'bullshit', 'bullshits', 'bullshitted', 'bullturds', 'bulok', 'bum', 'bum boy', 'bumblefuck', 'bung hole', 'bunghole', 'bunny fucker', 'bushit', 'busty', 'butt', 'butt fuck', 'butt plug', 'butt-pirate', 'buttcheeks', 'buttfuck', 'buttfucka', 'buttfucker', 'butthole', 'buttmuch', 'buttmunch', 'buttplug', 'c-0-c-k', 'c-o-c-k', 'c-u-n-t', 'c.0.c.k', 'c.o.c.k.', 'c.u.n.t', 'c0ck', 'c0cksucker', 'caca', 'cacafuego', 'camel toe', 'camgirl', 'camslut', 'camwhore', 'carpet muncher', 'carpetmuncher', 'cawk', 'chesticle', 'chi-chi man', 'child-fucker', 'chinc', 'chink', 'choad', 'chocolate rosebuds', 'chode', 'cipa', 'circlejerk', 'cl1t', 'cleveland steamer', 'clit', 'clit licker', 'clitface', 'clitfuck', 'clitoris', 'clits', 'clover clamps', 'clusterfuck', 'cnut', 'cock', 'cock sucker', 'cock-sucker', 'cockass', 'cockbite', 'cockburger', 'cockeye', 'cockface', 'cockfucker', 'cockhead', 'cockjockey', 'cockknoker', 'cocklump', 'cockmaster', 'cockmongler', 'cockmongruel', 'cockmonkey', 'cockmunch', 'cockmuncher', 'cocknose', 'cocknugget', 'cocks', 'cockshit', 'cocksmith', 'cocksmoke', 'cocksmoker', 'cocksniffer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cockwaffle', 'cok', 'cokmuncher', 'coksucka', 'coochie', 'coochy', 'coon', 'coons', 'cooter', 'coprolagnia', 'coprophilia', 'corksucker', 'cornhole', 'corp whore', 'cox', 'cracker', 'crackwhore', 'crap', 'creampie', 'crotte', 'cum', 'cumbubble', 'cumdumpster', 'cumguzzler', 'cumjockey', 'cummer', 'cumming', 'cums', 'cumshot', 'cumslut', 'cumtart', 'cunilingus', 'cunillingus', 'cunnie', 'cunnilingus', 'cunt', 'cuntass', 'cuntface', 'cunthole', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cuntrag', 'cunts', 'cuntslut', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'dago', 'dammit', 'damn', 'damned', 'damnit', 'darkie', 'darn', 'date rape', 'daterape', 'deep throat', 'deepthroat', 'deggo', 'dendrophilia', 'dick', 'dick head', 'dick hole', 'dick shy', 'dick-ish', 'dick-sneeze', 'dickbag', 'dickbeaters', 'dickdipper', 'dickface', 'dickflipper', 'dickfuck', 'dickfucker', 'dickhead', 'dickheads', 'dickhole', 'dickish', 'dickjuice', 'dickmilk', 'dickmonger', 'dicks', 'dickslap', 'dicksucker', 'dicksucking', 'dicktickler', 'dickwad', 'dickweasel', 'dickweed', 'dickwod', 'dike', 'dildo', 'dildos', 'dingleberries', 'dingleberry', 'dink', 'dinks', 'dipshit', 'dirsa', 'dirty pillows', 'dirty sanchez', 'dlck', 'dog style', 'dog-fucker', 'doggie style', 'doggiestyle', 'doggin', 'dogging', 'doggy style', 'doggystyle', 'dolcett', 'domination', 'dominatrix', 'dommes', 'donkey punch', 'donkeyribber', 'doochbag', 'dookie', 'doosh', 'double dong', 'double penetration', 'doublelift', 'douche', 'douche-fag', 'douchebag', 'douchewaffle', 'dp action', 'dry hump', 'duche', 'dumass', 'dumb ass', 'dumbass', 'dumbcunt', 'dumbfuck', 'dumbshit', 'dumshit', 'dvda', 'dyke', 'eat my ass', 'ecchi', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'erotic', 'erotism', 'escort', 'eunuch', 'f u c k', 'f u c k e r', 'f-u-c-k', 'f.u.c.k', 'f4nny', 'f_u_c_k', 'fag', 'fagbag', 'fagfucker', 'fagging', 'faggit', 'faggitt', 'faggot', 'faggotcock', 'faggs', 'fagot', 'fagots', 'fags', 'fagtard', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'fecal', 'feck', 'fecker', 'felch', 'felching', 'fellate', 'fellatio', 'feltch', 'female squirting', 'femdom', 'figging', 'fingerbang', 'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks', 'fingering', 'fist fuck', 'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks', 'fisting', 'flamer', 'flange', 'foah', 'fook', 'fooker', 'foot fetish', 'footjob', 'frotting', 'fuck', 'fuck buttons', 'fuck hole', 'fuck off', 'fuck puppet', 'fuck trophy', 'fuck yo mama', 'fuck you', 'fuck-ass', 'fuck-bitch', 'fuck-tard', 'fucka', 'fuckass', 'fuckbag', 'fuckboy', 'fuckbrain', 'fuckbutt', 'fuckbutter', 'fucked', 'fuckedup', 'fucker', 'fuckers', 'fuckersucker', 'fuckface', 'fuckhead', 'fuckheads', 'fuckhole', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fuckmeat', 'fucknugget', 'fucknut', 'fucknutt', 'fuckoff', 'fucks', 'fuckstick', 'fucktard', 'fucktards', 'fucktart', 'fucktoy', 'fucktwat', 'fuckup', 'fuckwad', 'fuckwhit', 'fuckwit', 'fuckwitt', 'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fuq', 'futanari', 'fux', 'fux0r', 'g-spot',
             'gabinulok', 'gang bang', 'gangbang', 'gangbanged', 'gangbangs', 'gassy ass', 'gay', 'gay sex', 'gayass', 'gaybob', 'gaydo', 'gayfuck', 'gayfuckist', 'gaylord', 'gaysex', 'gaytard', 'gaywad', 'genitals', 'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'goatcx', 'goatse', 'god damn', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'goddamnit', 'gokkun', 'golden shower', 'goo girl', 'gooch', 'goodpoop', 'gook', 'goregasm', 'gringo', 'grope', 'group sex', 'guido', 'guro', 'h0m0', 'h0mo', 'ham flap', 'hand job', 'handjob', 'hard core', 'hard on', 'hardcore', 'hardcoresex', 'he-she', 'heeb', 'hell', 'hentai', 'heshe', 'hircismus', 'ho', 'hoar', 'hoare', 'hoe', 'hoer', 'holy shit', 'hom0', 'homo', 'homodumbshit', 'homoerotic', 'honkey', 'hooker', 'hoor', 'hore', 'horniest', 'horny', 'hot carl', 'hot chick', 'hotsex', 'how to kill', 'how to murder', 'huge fat', 'humping', 'incest', 'intercourse', 'jack Off', 'jack-off', 'jackass', 'jackasses', 'jackhole', 'jackoff', 'jaggi', 'jagoff', 'jail bait', 'jailbait', 'jap', 'jelly donut', 'jerk off', 'jerk-off', 'jerkass', 'jigaboo', 'jiggaboo', 'jiggerboo', 'jism', 'jiz', 'jizm', 'jizz', 'juggs', 'jungle bunny', 'junglebunny', 'kawk', 'kike', 'kinbaku', 'kinkster', 'kinky', 'knob', 'knobbing', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kooch', 'kootch', 'kraut', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'kunja', 'kunt', 'kyke', 'l3i+ch', 'l3itch', 'labia', 'lameass', 'lardass', 'leather restraint', 'leather straight jacket', 'lemon party', 'lesbian', 'lesbo', 'lezzie', 'lmfao', 'lolita', 'lovemaking', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'make me come', 'male squirting', 'masochist', 'master-bate', 'masterb8', 'masterbat', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mcfagget', 'menage a trois', 'mick', 'middle finger', 'milf', 'minge', 'missionary position', 'mo-fo', 'mof0', 'mofo', 'moo foo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'mound of venus', 'mr hands', 'muff', 'muff diver', 'muffdiver', 'muffdiving', 'munging', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'naked', 'nambla', 'nawashi', 'nazi', 'negro', 'neonazi', 'nig nog', 'nigaboo', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'niglet', 'nimphomania', 'nipple', 'nipples', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'nsfw images', 'nude', 'nudity', 'numbnuts', 'nut sack', 'nutsack', 'nympho', 'nymphomania', 'octopussy', 'omorashi', 'one cup two girls', 'one guy one jar', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'orgy', 'p.u.s.s.y.', 'p0rn', 'paedophile', 'paki', 'panooch', 'panties', 'panty', 'pawn', 'pecker', 'peckerhead', 'pedobear', 'pedophile', 'pegging', 'penis', 'penisbanger', 'penisfucker', 'penispuffer', 'phone sex', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'piece of shit', 'pigfucker', 'pimpis', 'piss', 'piss off', 'piss pig', 'piss-off', 'pissed', 'pissed off', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'pisspig', 'piste', 'pisteng yawa', 'playboy', 'pleasure chest', 'pole smoker', 'polesmoker', 'pollock', 'ponyplay', 'poof', 'poon', 'poonani', 'poonany', 'poontang', 'poop', 'poop chute', 'poopchute', 'poopuncher', 'porch monkey', 'porchmonkey', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks', 'prince albert piercing', 'pron', 'pthc', 'pube', 'pubes', 'punanny', 'punany', 'puta', 'pusse', 'pussi', 'pussies', 'pussy', 'pussylicking', 'pussys', 'pust', 'puta', 'puto', 'queaf', 'queef', 'queer', 'queerbait', 'queerhole', 'quim', 'raghead', 'raging boner', 'rape', 'raping', 'rapist', 'rectum', 'renob', 'retard', 'reverse cowgirl', 'rimjaw', 'rimjob', 'rimming', 'rosy palm', 'rosy palm and her 5 sisters', 'rubbish', 'ruski', 'rusty trombone', 's&m', 's-o-b', 's.o.b.', 's0b', 'sadism', 'sadist', 'sand nigger', 'sandler', 'sandnigger', 'sanger', 'santorum', 'scat', 'schlong', 'scissoring', 'screwing', 'scroat', 'scrote', 'scrotum', 'segs', 'seggs', 'seks', 'semen', 'sex', 'sexo', 'sexy', 'shag', 'shagger', 'shaggin', 'shagging', 'shaved beaver', 'shaved pussy', 'shemale', 'shi+', 'shibari', 'shit', 'shit ass', 'shit fucker', 'shitass', 'shitbag', 'shitbagger', 'shitblimp', 'shitbrains', 'shitbreath', 'shitcanned', 'shitcunt', 'shitdick', 'shite', 'shiteater', 'shited', 'shitey', 'shitface', 'shitfaced', 'shitfuck', 'shitfull', 'shithead', 'shithole', 'shithouse', 'shiting', 'shitings', 'shits', 'shitspitter', 'shitstain', 'shitted', 'shitter', 'shitters', 'shittiest', 'shitting', 'shittings', 'shitty', 'shiz', 'shiznit', 'shota', 'shrimping', 'skank', 'skeet', 'skullfuck', 'slag', 'slanteye', 'slut', 'slutbag', 'sluts', 'smeg', 'smegma', 'smut', 'snatch', 'snowballing', 'sodomize', 'sodomy', 'son of a bitch', 'son of a whore', 'son-of-a-bitch', 'spac', 'spic', 'spick', 'splooge', 'splooge moose', 'spooge', 'spook', 'spread legs', 'spunk', 'strap on', 'strapon', 'strappado', 'strip club', 'style doggy', 'suck', 'suckass', 'sucks', 'suicide girls', 'sultry women', 'swastika', 'swinger', 't1tt1e5', 't1tties', 'tainted love', 'tard', 'taste my', 'tea bagging', 'teets', 'teez', 'testical', 'testicle', 'threesome', 'throating', 'thundercunt', 'tied up', 'tight white', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'titty', 'tittyfuck', 'tittywank', 'titwank', 'tongue in a', 'topless', 'tosser', 'towelhead', 'tranny', 'tribadism', 'tub girl', 'tubgirl', 'turd', 'tushy', 'tw4t', 'twat', 'twathead', 'twatlips', 'twats', 'twatty', 'twatwaffle', 'twink', 'twinkie', 'two fingers', 'two girls one cup', 'twunt', 'twunter', 'unclefucker', 'undressing', 'upskirt', 'urethra play', 'urophilia', 'v14gra', 'v1gra', 'va-j-j', 'vag', 'vagina', 'vajayjay', 'venus mound', 'viagra', 'vibrator', 'violet wand', 'vjayjay', 'vorarephilia', 'voyeur', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wankjob', 'wanky', 'wet dream', 'wetback', 'wh0re', 'wh0reface', 'white power', 'whoar', 'whore', 'whorebag', 'whoreface', 'willies', 'willy', 'wop', 'wrapping men', 'wrinkled starfish', 'xrated', 'xx', 'xxx', 'yaoi', 'yawa', 'yellow showers', 'yiffy', 'zoophilia', 'zubb']


class CheckProfanity():
    """Checks input for vulgar words

    `string: message` may take a parameter `message=string` which will show
    instead of `"not saved. Vulgar word/s found"`

    `boolean: enumerate_words`: if `True` shows all vulgar words found

    """

    def __init__(self, message=None, enumerate_words=False):

        if not message:
            self.message = "not saved. Vulgar word/s found"
        else:
            self.message = message

        self.enumerate_words = enumerate_words

    def __call__(self, form, field):

        result = [word for word in profanity if word in ("".join(word for word in str(
            field.data) if word.isalpha() or word.isnumeric() or word == " ")).split(" ")]

        if len(result) > 0:
            if self.message:
                raise ValidationError(self.message)

            if not self.message and self.enumerate_words:
                raise ValidationError(word for word in result.split(
                    ",") + (" are " if len(result) > 1 else " is ") + "not accepted")

            if self.message and self.enumerate_words:
                raise ValidationError(word for word in result.split(
                    ",") + (" are " if len(result) > 1 else " is ") + self.message)

        else:
            init(autoreset=True)
            print(f"CheckProfanity for {field.name}", "\033[1;32mpassed")


def check_profanity(text_to_check, message=None, enumerate_words=False):
    result = [word for word in profanity if word in ("".join(word for word in str(
        text_to_check) if word.isalpha() or word.isnumeric() or word == " ")).split(" ")]

    if len(result) > 0:
        if message:
            jsonify(failed=message)
            return False

        if not message and enumerate_words:
            jsonify(failed=(word for word in result.split(
                ",") + (" are " if len(result) > 1 else " is ") + "not accepted"))
            return False

        if message and enumerate_words:
            jsonify(failed=(word for word in result.split(
                ",") + (" are " if len(result) > 1 else " is ") + message))
            return False
        # needs fixing
    else:
        return True
