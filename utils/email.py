import re
'''
extract all emails from a raw text string s
'''
def extract_emails(s):
    pattern = "(?:[a-z0-9+!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    result = re.findall(pattern, s)
    return len(result)

# test 4 0 0 3 5
if __name__ == '__main__':
    print(extract_emails("""Peter Parker can be contacted at peter.parker@spiderman.com, while Mary Jane can be contacted at mary.jane@spiderman.com.
Venom’s Twitter username is @venom.123 and Carnage’s Instagram account is @carnage, but their email IDs are venom@spiderman.com and carnage@protonmail.com respectively.

There are other characters in the Spiderman Universe@Marvel, but they aren't very important in this context."""))
    print(extract_emails("""@Huzzah @The time has come @There are no emails in this text@"""))
    print(extract_emails("""A constant force, acting on a particle of mass m, will produce a constant acceleration a. Let us choose the x-axis to be in the common direction of F and a.
What is the work done by this force on the particle in causing a displacement x? We have, for constant acceleration, the relations a = ( V - v ) / t and x = ½ ( V + v ) t. Here v is the particle's speed at t = 0 and V is its speed at time t. The the work done is W = F x = m a x = m ( ( V - v ) / t ) ( ½ ( V + v ) ) t = ½ m V² - ½ m v². We call one-half the product of the mass of a body and the square of its speed the kinetic energy of the body. If we represent kinetic energy by the symbol K, then K = ½ m v². We may then state the above equation in this way:
The work done by the resultant force acting on a particle is equal to the change in the kinetic energy of the particle.

    """))
    print(extract_emails("""Vor dem Gesetz steht ein Türhüter. Zu diesem Türhüter kommt ein Mann vom Lande und bittet um Eintritt in das Gesetz. Aber der Türhüter sagt, daß er ihm jetzt den Eintritt nicht gewähren könne. Der Mann überlegt und fragt dann, ob er also später werde eintreten dürfen. "Es ist möglich", sagt der Türhüter, "jetzt aber nicht." Da das Tor zum Gesetz offensteht wie immer und der Türhüter beiseite tritt, bückt sich der Mann, um durch das Tor in das Innere zu@sehen.lop Als der Türhüter das merkt, lacht er und sagt: "Wenn es dich so lockt, versuche es doch, trotz meines Verbotes hineinzugehen. Merke aber: Ich bin mächtig. Und ich bin nur der unterste Türhüter. Von Saal zu Saal stehn aber Türhüter, einer mächtiger als der andere. Schon den Anblick des dritten kann nicht einmal ich mehr ertragen." Solche Schwierigkeiten hat der Mann vom Lande nicht erwartet; das Gesetz soll doch jedem und immer zugänglich sein, denkt er, aber als er jetzt den Türhüter in seinem Pelzmantel genauer@ansieht.seine große@Spitznase, den langen dünnen, schwarzen tatarischen Bart, entschließt er sich, doch lieber zu warten, bis er die Erlaubnis zum Eintritt bekommt. Der Türhüter@gibt.eu ihm einen Schemel und läßt ihn seitwärts von der Tür sich niedersetzen. Dort sitzt er Tage und Jahre.
"""))
    print(extract_emails("""abc@gmail.com;test1@gmail.com,absdcasd@hotmail.com:test33@yahoo.co.in|test555@yahoo.jp"""))