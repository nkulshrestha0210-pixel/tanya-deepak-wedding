document.addEventListener("DOMContentLoaded", () => {
  const audio = document.querySelector("#wedding-music");
  const musicToggle = document.querySelector("#music-toggle");
  const musicStatus = document.querySelector("#music-status");
  const setMusicUI = (playing) => {
    if (musicToggle) { musicToggle.textContent = playing ? "♫ Pause Din Shagna Da" : "♫ Play Din Shagna Da"; musicToggle.setAttribute("aria-pressed", String(playing)); }
    if (musicStatus) musicStatus.textContent = playing ? "Now playing · Din Shagna Da" : "Din Shagna Da · tap to play";
  };
  const playMusic = async () => { if (!audio) return; try { audio.volume = 0.42; await audio.play(); setMusicUI(true); } catch (_) { setMusicUI(false); if (musicStatus) musicStatus.textContent = "Tap Play Din Shagna Da to start"; } };
  if (audio) { audio.loop = true; audio.addEventListener("play", () => setMusicUI(true)); audio.addEventListener("pause", () => setMusicUI(false)); audio.addEventListener("error", () => { if (musicStatus) musicStatus.textContent = "Music could not load — check the audio file"; }); }
  // Pull-to-navigate rope: dragging the golden thread down opens the next page.
  let ropeDrag = null;
  document.addEventListener("pointerdown", (e) => {
    const rope = e.target.closest(".grandparents-rope");
    if (!rope || e.button !== 0) return;
    ropeDrag = { rope, startY: e.clientY, pointerId: e.pointerId, moved: false };
    rope.classList.add("rope-being-pulled");
    try { rope.setPointerCapture(e.pointerId); } catch (_) {}
  });
  document.addEventListener("pointermove", (e) => {
    if (!ropeDrag || e.pointerId !== ropeDrag.pointerId) return;
    const delta = Math.max(0, Math.min(95, e.clientY - ropeDrag.startY));
    if (delta > 4) ropeDrag.moved = true;
    ropeDrag.rope.style.setProperty("--rope-pull", `${delta}px`);
  });
  document.addEventListener("pointerup", (e) => {
    if (!ropeDrag || e.pointerId !== ropeDrag.pointerId) return;
    const { rope, startY } = ropeDrag;
    const distance = e.clientY - startY;
    const dragged = ropeDrag.moved;
    rope.classList.remove("rope-being-pulled");
    ropeDrag = null;
    if (dragged && distance >= 48) {
      rope.classList.add("rope-pull-complete");
      rope.dataset.pullConfirmed = "true";
      setTimeout(() => { rope.click(); }, 120);
    } else {
      rope.style.setProperty("--rope-pull", "0px");
      if (dragged) rope.classList.add("rope-pull-return");
      setTimeout(() => rope.classList.remove("rope-pull-return"), 280);
    }
  });
  document.addEventListener("pointercancel", () => {
    if (ropeDrag) { ropeDrag.rope.classList.remove("rope-being-pulled"); ropeDrag.rope.style.setProperty("--rope-pull", "0px"); ropeDrag = null; }
  });
  document.addEventListener("click", (e) => {
    const rope = e.target.closest(".grandparents-rope");
    if (!rope) return;
    if (rope.dataset.pullConfirmed === "true") { delete rope.dataset.pullConfirmed; return; }
    // A tap is deliberately not enough; the guest must physically pull the thread.
    e.preventDefault();
  }, true);

  // Event delegation means the music control and envelope continue to work after in-page transitions.
  document.addEventListener("click", async (e) => {
    const toggle = e.target.closest("#music-toggle");
    if (toggle && audio) { e.preventDefault(); if (audio.paused) await playMusic(); else audio.pause(); return; }
    const envelope = e.target.closest("#open-envelope");
    if (envelope) { envelope.classList.add("envelope-opening"); envelope.setAttribute("aria-label", "Wedding invitation opened"); const hint=document.querySelector("#envelope-hint"); if(hint) hint.textContent="Your invitation is open — enjoy the music"; await playMusic(); return; }
  });

  let transitionCount = 0;
  const overlay = document.createElement('div'); overlay.className='page-transition-overlay'; overlay.setAttribute('aria-hidden','true'); overlay.innerHTML='<span class="transition-ornament">✦</span><span class="transition-caption">Tanya &amp; Deepak</span>'; document.body.appendChild(overlay);
  function initPage() {
    document.body.classList.add('reveal-ready');
    const navButton=document.querySelector('.menu-toggle'), nav=document.querySelector('#primary-nav');
    if(navButton && nav) navButton.onclick=()=>{const open=nav.classList.toggle('nav-open');navButton.setAttribute('aria-expanded',String(open));};
    document.querySelectorAll('.section, .event-teaser, .family-panel, .detail-card, .closing-card, .venue-layout, .rsvp-layout, .countdown-section, .event-detail-card, .hero-frame').forEach((item,index)=>{item.classList.add('reveal-on-scroll'); if(item.classList.contains('event-teaser')) item.style.transitionDelay=(index%5)*70+'ms';});
    if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');observer.unobserve(entry.target);}}),{threshold:.08});document.querySelectorAll('.reveal-on-scroll').forEach(item=>observer.observe(item));}else document.querySelectorAll('.reveal-on-scroll').forEach(item=>item.classList.add('is-visible'));
    const countdown=document.querySelector('[data-countdown]'); if(countdown){const target=new Date(countdown.dataset.countdown).getTime();const update=()=>{let r=Math.max(0,target-Date.now());const vals={days:Math.floor(r/86400000),hours:Math.floor(r%86400000/3600000),minutes:Math.floor(r%3600000/60000),seconds:Math.floor(r%60000/1000)};Object.entries(vals).forEach(([u,v])=>{const n=countdown.querySelector(`[data-unit="${u}"]`);if(n)n.textContent=String(v).padStart(2,'0');});};update();if(countdown._timer)clearInterval(countdown._timer);countdown._timer=setInterval(update,1000);}
    const slides=document.querySelector('.event-teasers'); if(slides){if(slides._autoTimer)clearInterval(slides._autoTimer);const cards=Array.from(slides.querySelectorAll('.event-teaser'));if(cards.length>1){let i=0;slides._autoTimer=setInterval(()=>{if(document.hidden)return;i=(i+1)%cards.length;slides.scrollTo({left:cards[i].offsetLeft-cards[0].offsetLeft,behavior:'smooth'});},3500);}}
    const progress=document.querySelector('.scroll-progress')||document.createElement('div');progress.className='scroll-progress';progress.setAttribute('aria-hidden','true');if(!progress.isConnected)document.body.appendChild(progress);const updateProgress=()=>{const max=document.documentElement.scrollHeight-innerHeight;progress.style.width=(max>0?Math.min(100,scrollY/max*100):0)+'%';};window.onscroll=updateProgress;updateProgress();
    document.querySelectorAll('#primary-nav a').forEach(a=>{const u=new URL(a.href,location.href);a.toggleAttribute('aria-current',u.pathname===location.pathname);if(u.pathname===location.pathname)a.setAttribute('aria-current','page');});
  }
  initPage();
  // Fetch internal pages into the existing document. The single <audio> element is NOT replaced,
  // so the song continues seamlessly while page content flips or the golden thread pulls across.
  document.addEventListener('click', async (e)=>{
    const link=e.target.closest('a[href]'); if(!link || e.defaultPrevented || e.button!==0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || link.target==='_blank' || link.hasAttribute('download')) return;
    const url=new URL(link.href,location.href); if(url.origin!==location.origin || url.pathname===location.pathname && url.search===location.search || link.getAttribute('href').startsWith('#')) return;
    if(!['http:','https:'].includes(url.protocol))return;
    e.preventDefault(); transitionCount++; const mode=link.classList.contains('page-turn-thread') || transitionCount%2===0?'thread':'flip';
    document.body.classList.remove('transition-flip','transition-thread'); document.body.classList.add('transition-'+mode); overlay.classList.add('active');
    try { const response=await fetch(url.href,{headers:{'X-Requested-With':'WeddingPageTransition'}}); if(!response.ok)throw new Error('Page load failed'); const html=await response.text();const doc=new DOMParser().parseFromString(html,'text/html');const newMain=doc.querySelector('#main-content');const oldMain=document.querySelector('#main-content');if(!newMain||!oldMain)throw new Error('Missing page content');
      oldMain.innerHTML=newMain.innerHTML;
      document.title=doc.title;history.pushState({url:url.href},'',url.href);window.scrollTo({top:0,behavior:'instant'});initPage();
      // Brief, animated page-turn/thread-pull cover; music element remains untouched.
      setTimeout(()=>{overlay.classList.remove('active');document.body.classList.remove('transition-flip','transition-thread');},650);
    } catch(err) { location.href=url.href; }
  });
  window.addEventListener('popstate',async()=>{try{const r=await fetch(location.href,{headers:{'X-Requested-With':'WeddingPageTransition'}});if(!r.ok)throw new Error();const d=new DOMParser().parseFromString(await r.text(),'text/html');const m=d.querySelector('#main-content');if(!m)throw new Error();document.querySelector('#main-content').innerHTML=m.innerHTML;document.title=d.title;initPage();window.scrollTo({top:0,behavior:'instant'});}catch(_){location.reload();}});
});
