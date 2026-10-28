(function(){var d=document,r=d.documentElement;
function setIcon(){d.querySelectorAll('[data-theme-toggle]').forEach(function(b){b.innerHTML='<i data-lucide="'+(r.dataset.theme==='light'?'moon':'sun')+'" style="width:16px;height:16px"></i>'});if(window.lucide)lucide.createIcons()}
d.querySelectorAll('[data-theme-toggle]').forEach(function(b){b.addEventListener('click',function(){r.dataset.theme=r.dataset.theme==='light'?'dark':'light';try{localStorage.setItem('theme',r.dataset.theme)}catch(e){}setIcon()})});
d.querySelectorAll('[data-menu]').forEach(function(b){b.addEventListener('click',function(){d.querySelector('.nav').classList.toggle('open')})});
d.querySelectorAll('.mobile-menu a').forEach(function(a){a.addEventListener('click',function(){d.querySelector('.nav').classList.remove('open')})});
var f=d.getElementById('contact-form');if(f)f.addEventListener('submit',function(e){e.preventDefault();var v=function(n){return(f.elements[n]&&f.elements[n].value||'').trim()};
var msg='Hi Muneez, I am '+v('name')+' ('+v('email')+', '+v('code')+' '+v('phone')+').'+(v('service')?' Interested in: '+v('service')+'.':'')+(v('message')?' '+v('message'):'');
window.open('https://wa.me/971569623049?text='+encodeURIComponent(msg),'_blank');var ok=d.getElementById('contact-ok');if(ok){ok.hidden=false;f.hidden=true}});
setIcon();if(!window.lucide){var t=setInterval(function(){if(window.lucide){clearInterval(t);lucide.createIcons()}},100)}})();

(function(){var d=document;var bar=d.createElement('div');bar.className='progress';d.body.appendChild(bar);
var nav=d.querySelector('.nav');addEventListener('scroll',function(){var h=d.documentElement;bar.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%';if(nav)nav.classList.toggle('scrolled',scrollY>8)},{passive:true});
if(!('IntersectionObserver' in window))return;
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
d.querySelectorAll('main section:not(.hero) .h2, main section:not(.hero) .lead, main section:not(.hero) .card, main section:not(.hero) .list li, main section:not(.hero) .steps li, main section:not(.hero) .faq, main section:not(.hero) .chip, main section:not(.hero) article').forEach(function(el){var i=el.parentElement?Array.prototype.indexOf.call(el.parentElement.children,el):0;el.style.transitionDelay=Math.min(i,6)*70+'ms';el.classList.add('rv');io.observe(el)});
})();
