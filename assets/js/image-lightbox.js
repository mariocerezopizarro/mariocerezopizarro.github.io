(function(){
  const candidates=[...document.querySelectorAll('.note-image, .gallery-grid img, .entry-gallery img, .note-image-link img')];
  const images=candidates.filter((img,index,arr)=>{
    if(arr.indexOf(img)!==index)return false;
    const link=img.closest('a');
    if(link&&link.classList.contains('note-image-link')){
      const href=link.getAttribute('href')||'';
      if(!/\.(png|jpe?g|webp|avif|gif|svg)(?:[?#]|$)/i.test(href))return false;
    }
    return true;
  });
  if(!images.length)return;

  const style=document.createElement('style');
  style.textContent=`
    .site-zoomable{cursor:zoom-in}
    .site-zoomable:focus-visible{outline:3px solid #168ee8;outline-offset:4px}
    .site-image-viewer[hidden]{display:none!important}
    .site-image-viewer{position:fixed;inset:0;z-index:10050;background:rgba(0,15,32,.94);backdrop-filter:blur(8px);display:grid;grid-template-rows:auto 1fr auto;padding:16px}
    .site-image-viewer-top{display:flex;justify-content:flex-end}
    .site-image-viewer-close{width:44px;height:44px;border:0;border-radius:50%;background:rgba(255,255,255,.14);color:#fff;font-size:28px;cursor:pointer}
    .site-image-viewer-stage{min-height:0;display:grid;place-items:center;padding:8px}
    .site-image-viewer-img{display:block;max-width:min(96vw,1600px);max-height:82vh;width:auto;height:auto;object-fit:contain;border-radius:10px;box-shadow:0 18px 60px rgba(0,0,0,.45)}
    .site-image-viewer-caption{margin:8px auto 0;max-width:1000px;color:#eef8ff;text-align:center;font:14px/1.5 system-ui,sans-serif}
    body.site-image-viewer-open{overflow:hidden}
  `;
  document.head.appendChild(style);

  const viewer=document.createElement('div');
  viewer.className='site-image-viewer';
  viewer.hidden=true;
  viewer.innerHTML='<div class="site-image-viewer-top"><button class="site-image-viewer-close" type="button" aria-label="Cerrar imagen ampliada">×</button></div><div class="site-image-viewer-stage"><img class="site-image-viewer-img" alt=""></div><div class="site-image-viewer-caption"></div>';
  document.body.appendChild(viewer);

  const big=viewer.querySelector('.site-image-viewer-img');
  const caption=viewer.querySelector('.site-image-viewer-caption');
  const close=viewer.querySelector('.site-image-viewer-close');
  let returnFocus=null;

  function open(img){
    returnFocus=document.activeElement;
    const link=img.closest('a');
    const linkedImage=link&&/\.(png|jpe?g|webp|avif|gif|svg)(?:[?#]|$)/i.test(link.getAttribute('href')||'') ? link.href : '';
    big.src=linkedImage||img.currentSrc||img.src;
    big.alt=img.alt||'Imagen ampliada';
    caption.textContent=img.alt||'';
    viewer.hidden=false;
    document.body.classList.add('site-image-viewer-open');
    close.focus();
  }
  function hide(){
    if(viewer.hidden)return;
    viewer.hidden=true;
    document.body.classList.remove('site-image-viewer-open');
    big.removeAttribute('src');
    if(returnFocus&&typeof returnFocus.focus==='function')returnFocus.focus();
  }

  images.forEach(img=>{
    img.classList.add('site-zoomable');
    if(!img.hasAttribute('tabindex'))img.tabIndex=0;
    if(!img.hasAttribute('role'))img.setAttribute('role','button');
    if(!img.hasAttribute('aria-label'))img.setAttribute('aria-label','Ampliar imagen');
    img.addEventListener('click',e=>{
      const link=img.closest('a');
      if(link&&link.classList.contains('note-image-link')){
        e.preventDefault();
        e.stopPropagation();
      }
      open(img);
    });
    img.addEventListener('keydown',e=>{
      if(e.key==='Enter'||e.key===' '){
        e.preventDefault();
        open(img);
      }
    });
  });

  close.addEventListener('click',hide);
  viewer.addEventListener('click',e=>{if(e.target===viewer||e.target.classList.contains('site-image-viewer-stage'))hide()});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!viewer.hidden)hide()});
})();