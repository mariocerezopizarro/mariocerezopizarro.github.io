from pathlib import Path

p = Path('index.html')
text = p.read_text(encoding='utf-8')
needle = '''    </article>\n  </div>\n  <div class="archive-action"><a href="jugando.html">Ver todo mi historial de juego <span aria-hidden="true">→</span></a></div>\n</section>'''
insert = '''    </article>\n    <article class="note-card">\n      <div class="note-meta"><span>JUGADO RECIENTEMENTE · VIDEOJUEGOS</span><span>PlayStation · Septiembre 2026</span></div>\n      <h3>Death Stranding 2: la prisa no es un buen aliado</h3>\n      <p>Este mes he estado jugando a <strong>Death Stranding 2</strong> en PlayStation. Al igual que en la primera entrega, sorprende y gusta por sus mecánicas: aquí la prisa no es un buen aliado. Su narrativa es profundamente sorprendente y contar con intérpretes reales supone un plus enorme para la inmersión. He buscado alcanzar el Platino para descubrir todo lo que el equipo de desarrollo había pensado para quienes jugamos. Una obra maestra de Kojima que redefine la forma en la que nos relacionamos con los videojuegos. <strong>¡Soy Sam!</strong></p>\n    </article>\n  </div>\n  <div class="archive-action"><a href="jugando.html">Ver todo mi historial de juego <span aria-hidden="true">→</span></a></div>\n</section>'''
start = text.find('<section class="cuaderno section" id="jugando">')
if start == -1:
    raise SystemExit('No se encontró la sección jugando')
pos = text.find(needle, start)
if pos == -1:
    raise SystemExit('No se encontró el cierre esperado de la sección jugando')
text = text[:pos] + text[pos:].replace(needle, insert, 1)
p.write_text(text, encoding='utf-8')
