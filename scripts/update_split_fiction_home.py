from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

old = '''    <article class="note-card note-featured">
      <div class="note-meta"><span>JUGANDO AHORA · VIDEOJUEGOS</span><span>PlayStation · Septiembre 2026</span></div>
      <h3>Death Stranding 2: la prisa no es un buen aliado</h3>
      <p>Este mes estoy jugando a <strong>Death Stranding 2</strong> en PlayStation. Al igual que en la primera entrega, sorprende y gusta por sus mecánicas: aquí la prisa no es un buen aliado. Su narrativa es profundamente sorprendente y contar con intérpretes reales supone un plus enorme para la inmersión. He buscado alcanzar el Platino para descubrir todo lo que el equipo de desarrollo había pensado para quienes jugamos. Una obra maestra de Kojima que redefine la forma en la que nos relacionamos con los videojuegos. <strong>¡Soy Sam!</strong></p>
    </article>'''

new = '''    <article class="note-card note-featured">
      <div class="note-meta"><span>JUGANDO AHORA · VIDEOJUEGOS</span><span>PlayStation · Octubre 2026</span></div>
      <h3>Split Fiction: volver a jugar juntos</h3>
      <div class="note-body"><p>Este mes estoy jugando a <strong>Split Fiction</strong>, la última aventura cooperativa de Hazelight Studios. Mio y Zoe son dos escritoras muy diferentes: una escribe ciencia ficción y la otra fantasía. Tras ser conectadas a una máquina diseñada para apropiarse de sus ideas, quedan atrapadas dentro de sus propias historias y tendrán que colaborar para escapar, saltando continuamente entre mundos fantásticos y escenarios de ciencia ficción.<br><br>Pero lo que más me está gustando es otra cosa. En una época en la que el multijugador parece casi inevitablemente asociado a jugar online, Hazelight sigue reivindicando el placer de <strong>jugar juntos, en la misma pantalla y en el mismo sofá</strong>. La cooperación no es un añadido: hablar, coordinarse, equivocarse y avanzar con otra persona forman parte de la propia experiencia narrativa. <strong>A veces, jugar juntos sigue siendo la mejor forma de jugar.</strong></p><a class="note-image-link" href="the-final-level-in-split-fiction.avif" target="_blank" rel="noopener" aria-label="Ampliar imagen del capítulo final de Split Fiction"><img src="the-final-level-in-split-fiction.avif" alt="Escena del capítulo final de Split Fiction en pantalla dividida, con los mundos de ciencia ficción y fantasía compartiendo la pantalla" loading="lazy" decoding="async"><span>Ampliar imagen ↗</span></a></div>
    </article>'''

if old not in text:
    raise SystemExit("No se encontró la entrada de Death Stranding 2 en la portada")

p.write_text(text.replace(old, new, 1), encoding="utf-8")
