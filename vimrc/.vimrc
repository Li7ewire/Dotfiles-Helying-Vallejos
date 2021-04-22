" Plugins will be downloaded under the specified directory.
call plug#begin('~/.vim/plugged')

" Declare the list of plugins.
 set laststatus=2
"Polyglot Syntax Plugin
Plug 'sheerun/vim-polyglot'
"One Dark Colorscheme
Plug 'joshdick/onedark.vim'
"Dracula Colorscheme
Plug 'dracula/vim', { 'as': 'dracula' }
"Edge Colorscheme
Plug 'sainnhe/edge'
"Palenight Colorscheme
Plug 'drewtempelmeyer/palenight.vim'
"Challenger Deep Colorscheme
Plug 'challenger-deep-theme/vim', { 'as': 'challenger-deep' }
"Onehalf Colorscheme
Plug 'sonph/onehalf', {'rtp': 'vim/'}
"Colorscheme Pack
Plug 'flazz/vim-colorschemes'
"Lightline Status Bar Plugin
Plug 'itchyny/lightline.vim'
"Nerd Tree File Manager
Plug 'scrooloose/nerdtree', {'on': 'NERDTreeToggle'}
"Autopairs
Plug 'jiangmiao/auto-pairs'
"Rainbow Brackets Color Plugin
Plug 'luochen1990/rainbow'
"Indent Lines Indicators
Plug 'yggdroot/indentline'
"Distraction Free Mode Plugin
Plug 'junegunn/goyo.vim'
"VSCode Autocomplete
Plug 'neoclide/coc.nvim', {'branch': 'release'}
"Syntax Checking Plugin
"Plug 'scrooloose/syntastic'
"CtrlP
Plug 'ctrlpvim/ctrlp.vim'
"Code Minimap Plugin
Plug 'severin-lemaignan/vim-minimap'
"Icons
Plug 'ryanoasis/vim-devicons'
"Ends Vim Plug Call
call plug#end()


colorscheme nord
let g:airline_theme='onedark'
"Disables special character rendering at end of line
set nolist
"Enables line numbers
set number
set number relativenumber

"Enable Rainbow Brackets
let g:rainbow_active = 1
