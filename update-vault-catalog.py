#!/usr/bin/env python3
"""Refresh Vault catalog from the files under vault/files (no third-party dependencies)."""
from pathlib import Path
import json,mimetypes
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'vault'/'files'
CAT=ROOT/'vault'/'catalog.js'
category_map={'logos':'Brand Assets','photography':'Brand Assets','icons':'Brand Assets','illustrations':'Brand Assets','fonts':'Brand Assets','guides':'Brand Assets','templates':'Templates','documents':'Documents','project-examples':'Documents'}
preview_ext={'.svg','.png','.jpg','.jpeg','.gif','.webp','.pdf'}
ignore={'README.txt','.DS_Store','Thumbs.db','.gitkeep'}
items=[]
for path in sorted(BASE.rglob('*')):
 if not path.is_file() or path.name in ignore or path.name.startswith('.'):
  continue
 relative=path.relative_to(BASE)
 cat=category_map.get(relative.parts[0],'Documents')
 title=path.stem.replace('_',' ').replace('-',' ').strip()
 ext=path.suffix.lower()
 items.append({'id':f'VA-{len(items)+1:04d}','title':title,'category':cat,'description':f'{relative.parent.as_posix()} · {ext[1:].upper() or "File"} asset','path':'vault/files/'+relative.as_posix(),'type':ext[1:].upper() or 'FILE','preview':ext in preview_ext,'demo':False})
CAT.write_text('window.BEDROCK_VAULT_ITEMS = '+json.dumps(items,indent=2,ensure_ascii=False)+';\n',encoding='utf-8')
print(f'Updated {CAT.relative_to(ROOT)} with {len(items)} assets.')
