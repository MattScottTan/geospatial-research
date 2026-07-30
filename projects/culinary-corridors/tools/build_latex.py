#!/usr/bin/env python3
"""Convert BUILD_INSTRUCTIONS_v8.md (paste-as-you-go script) to LaTeX preview."""
import re
import sys

SOURCE = '/home/claude/work/BUILD_INSTRUCTIONS.md'
OUT = '/home/claude/storymap_preview.tex'

LATEX_HEADER = r"""\documentclass[11pt]{article}
\usepackage[a4paper, margin=2.2cm]{geometry}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\usepackage{graphicx}
\usepackage{float}
\usepackage{microtype}
\usepackage{caption}
\usepackage[hidelinks,breaklinks]{hyperref}
\usepackage{xurl}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{parskip}
\usepackage{setspace}
\setstretch{1.18}

% Caption styling — italicize and slightly smaller, like StoryMap
\captionsetup{
  font={small,it},
  labelfont={small,bf,up},
  labelsep=period,
  justification=justified,
  singlelinecheck=false,
  margin=0pt
}

% Section heading: large, bold, with extra space above (no horizontal rule)
\makeatletter
\renewcommand\section{\@startsection{section}{1}{\z@}%
  {1.6em \@plus 0.4em \@minus 0.2em}%
  {0.6em}%
  {\normalfont\Large\bfseries\color{black!85}}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
  {1.2em \@plus 0.3em \@minus 0.1em}%
  {0.4em}%
  {\normalfont\large\bfseries\itshape\color{black!75}}}
\makeatother

% Pull-quote style (matches the StoryMap quote block)
\newenvironment{pullquote}
  {\begin{quote}\itshape\color{black!72}\hspace*{-0.4em}\rule{2pt}{1em}\hspace{0.6em}}
  {\end{quote}}

% Soft section break — vertical only, no horizontal-mode commands
\newcommand{\sectionbreak}{%
  \par\nobreak\vspace{0.8em}%
  \par\centerline{\textcolor{black!40}{$\bullet$\quad$\bullet$\quad$\bullet$}}%
  \par\vspace{0.6em}\nobreak%
}

\renewcommand{\refname}{Bibliography}

\title{\vspace{-2em}\Huge\bfseries Cuisine resemblance has a shape\\ that distance can't predict\\[0.4em]
       \large\mdseries\itshape Mapping the residual network that connects archipelagos, peninsulas, and Atlantic shores}
\author{Matthew Scott Tan \\[0.4em]
        \normalsize\itshape Howard T.~Fisher Prize in GIS submission \,\textbullet\, Harvard CGA}
\date{May 2026}

\begin{document}
\maketitle

\noindent\textit{This is a preview-only PDF of the StoryMap content. The published version
will render block-by-block in ArcGIS StoryMaps with the same prose, figures, captions, and
bibliography. Use this file to verify flow, sequencing, and figure placement before pasting
into the ArcGIS editor.}

\vspace{1em}
\noindent\hrulefill

"""

LATEX_FOOTER = r"""
\end{document}
"""


def escape_latex(s):
    """Escape LaTeX special characters in plain text."""
    # Order matters here.
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]
    for old, new in replacements:
        s = s.replace(old, new)
    # Unicode em/en dashes — keep as-is (XeLaTeX handles them)
    return s


URL_RE = re.compile(r'(https?://[^\s,)\]]+)')

def render_text(s):
    """Convert text to LaTeX, wrapping URLs in \\url{} so xurl can break them."""
    parts = URL_RE.split(s)
    out = []
    for part in parts:
        if URL_RE.match(part):
            # Strip any trailing punctuation that shouldn't be inside the URL
            tail = ''
            while part and part[-1] in '.,;:':
                tail = part[-1] + tail
                part = part[:-1]
            out.append(r'\url{' + part + '}')
            if tail:
                out.append(escape_latex(tail))
        else:
            out.append(escape_latex(part))
    return ''.join(out)


def parse_build_doc(text):
    """Walk through the build doc and emit LaTeX blocks in order."""
    lines = text.split('\n')
    out = []
    i = 0
    last_image = None

    # Skip front matter — start at the first "# SECTION" or "# COVER"
    while i < len(lines) and not (lines[i].startswith('# COVER') or lines[i].startswith('# SECTION')):
        i += 1

    while i < len(lines):
        raw = lines[i]
        line = raw.strip()

        # Section markers in build doc — used for our own progress, not output
        if line.startswith('# COVER') or line.startswith('# SECTION'):
            i += 1
            continue

        # Skip horizontal rules
        if line == '---':
            i += 1
            continue

        # Skip the trailing "Quick reference" table and end matter
        if line.startswith('# Quick reference') or line.startswith('*End of build instructions'):
            break

        # Image directive
        if 'Image block' in line and 'Upload' in line:
            m = re.search(r'Upload `([^`]+)`', line)
            if m:
                last_image = m.group(1)
            i += 1
            continue

        # Caption directive — capture the next fenced block as the figure caption
        if line.startswith('> **➤ Caption'):
            i += 1
            # advance to opening ```
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                i += 1
            if i >= len(lines):
                break
            i += 1  # past opening ```
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1  # past closing ```
            caption = '\n'.join(buf).strip()

            if last_image:
                out.append('')
                out.append(r'\begin{figure}[H]')
                out.append(r'  \centering')
                out.append(rf'  \includegraphics[width=\linewidth,keepaspectratio]{{figures/{last_image}}}')
                out.append(rf'  \caption{{{render_text(caption)}}}')
                out.append(r'\end{figure}')
                out.append('')
                last_image = None
            continue

        # Alt text directive — skip it AND its fenced block (no LaTeX equivalent needed for preview)
        if line.startswith('> **➤ Alt text'):
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                i += 1
            if i >= len(lines):
                break
            i += 1  # past opening
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                i += 1
            i += 1  # past closing
            continue

        # Separator — emit a soft rule between sections
        if line.startswith('> **➤ Click `+` → Separator'):
            out.append('')
            out.append(r'\sectionbreak')
            out.append('')
            i += 1
            continue

        # Heading H2 — section
        if 'Heading (H2)' in line:
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                i += 1
            if i >= len(lines):
                break
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1
            heading = '\n'.join(buf).strip()
            out.append('')
            out.append(rf'\section*{{{escape_latex(heading)}}}')
            out.append(rf'\addcontentsline{{toc}}{{section}}{{{escape_latex(heading)}}}')
            out.append('')
            continue

        # Heading H3 — subsection (case-study cuisines)
        if 'Heading (H3)' in line:
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                i += 1
            if i >= len(lines):
                break
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1
            heading = '\n'.join(buf).strip()
            out.append('')
            out.append(rf'\subsection*{{{escape_latex(heading)}}}')
            out.append('')
            continue

        # Heading H1 — cover title
        if 'Heading (H1)' in line:
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                i += 1
            if i >= len(lines):
                break
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1
            # Already in the title block; skip - the title was set in the header
            continue

        # Text block
        if 'Text block' in line:
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                i += 1
            if i >= len(lines):
                break
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1
            text = '\n'.join(buf).strip()
            # Split on blank lines into paragraphs, escape each
            paras = re.split(r'\n\s*\n', text)
            for p in paras:
                p = p.strip()
                if not p:
                    continue
                out.append('')
                out.append(render_text(p))
                out.append('')
            continue

        # Quote block
        if 'Quote block' in line:
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                i += 1
            if i >= len(lines):
                break
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1
            text = '\n'.join(buf).strip()
            out.append('')
            out.append(r'\begin{pullquote}')
            out.append(render_text(text))
            out.append(r'\end{pullquote}')
            out.append('')
            continue

        i += 1

    return '\n'.join(out)


def main():
    with open(SOURCE) as f:
        src = f.read()
    body = parse_build_doc(src)
    with open(OUT, 'w') as f:
        f.write(LATEX_HEADER)
        f.write(body)
        f.write(LATEX_FOOTER)
    print(f'Wrote {OUT}')
    print(f'Length: {len(body.split(chr(10)))} lines body, {len(body)} chars')


if __name__ == '__main__':
    main()
