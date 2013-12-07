# revision 20679
# category Package
# catalog-ctan /macros/latex/contrib/ticket
# catalog-date 2010-12-06 20:55:11 +0100
# catalog-license lppl
# catalog-version 0.4b
Name:		texlive-ticket
Version:	0.4b
Release:	3
Summary:	Make labels, visting-cards, pins with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ticket
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ticket.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ticket.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides an easy to handle interface to produce visiting cards,
labels for your files, stickers, pins and other stuff for your
office, conferences etc. All you need is a definition of your
'ticket' included in a ticket definition file and the two
commands \ticketdefault and \ticket.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ticket/aj8414.tdf
%{_texmfdistdir}/tex/latex/ticket/dura5222.tdf
%{_texmfdistdir}/tex/latex/ticket/flashCard.tdf
%{_texmfdistdir}/tex/latex/ticket/freepin.tdf
%{_texmfdistdir}/tex/latex/ticket/freepin2.tdf
%{_texmfdistdir}/tex/latex/ticket/freepin3.tdf
%{_texmfdistdir}/tex/latex/ticket/he4432.tdf
%{_texmfdistdir}/tex/latex/ticket/lz1680.tdf
%{_texmfdistdir}/tex/latex/ticket/lz1681.tdf
%{_texmfdistdir}/tex/latex/ticket/lz1685.tdf
%{_texmfdistdir}/tex/latex/ticket/ticket.sty
%{_texmfdistdir}/tex/latex/ticket/zw32010.tdf
%{_texmfdistdir}/tex/latex/ticket/zw3424.tdf
%{_texmfdistdir}/tex/latex/ticket/zw4752.tdf
%doc %{_texmfdistdir}/doc/latex/ticket/README
%doc %{_texmfdistdir}/doc/latex/ticket/comment
%doc %{_texmfdistdir}/doc/latex/ticket/ex_file.pdf
%doc %{_texmfdistdir}/doc/latex/ticket/ex_file.tex
%doc %{_texmfdistdir}/doc/latex/ticket/ex_flashcard.pdf
%doc %{_texmfdistdir}/doc/latex/ticket/ex_flashcard.tex
%doc %{_texmfdistdir}/doc/latex/ticket/ex_flashcard_dup.pdf
%doc %{_texmfdistdir}/doc/latex/ticket/ex_flashcard_rm.pdf
%doc %{_texmfdistdir}/doc/latex/ticket/ex_flashcard_rm.tex
%doc %{_texmfdistdir}/doc/latex/ticket/ex_marks.pdf
%doc %{_texmfdistdir}/doc/latex/ticket/ex_marks.tex
%doc %{_texmfdistdir}/doc/latex/ticket/ex_pin.pdf
%doc %{_texmfdistdir}/doc/latex/ticket/ex_pin.tex
%doc %{_texmfdistdir}/doc/latex/ticket/ex_vcard.pdf
%doc %{_texmfdistdir}/doc/latex/ticket/ex_vcard.tex
%doc %{_texmfdistdir}/doc/latex/ticket/manual.pdf
%doc %{_texmfdistdir}/doc/latex/ticket/manual.tex
%doc %{_texmfdistdir}/doc/latex/ticket/test.tex
%doc %{_texmfdistdir}/doc/latex/ticket/words.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4b-2
+ Revision: 756843
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4b-1
+ Revision: 719740
- texlive-ticket
- texlive-ticket
- texlive-ticket

