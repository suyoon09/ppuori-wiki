'use client';

export default function FlowLines() {
    // Abstract flow-field lines — topographic/geometric, flowing gently downward
    // These are purely decorative, very faint
    return (
        <svg
            viewBox="0 0 400 900"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="xMidYMid slice"
            style={{ width: '100%', height: '100%' }}
        >
            <g stroke="#2C2C2C" strokeWidth="0.6" opacity="1">
                {/* Central descending curves */}
                <path d="M200 0 C200 60, 195 120, 190 200 C185 280, 175 340, 168 440 C162 520, 158 620, 155 750 C153 820, 150 860, 148 900" />
                <path d="M200 0 C200 50, 208 130, 215 220 C222 310, 230 380, 238 480 C244 560, 250 660, 253 780 C255 840, 258 870, 260 900" />

                {/* Left branching */}
                <path d="M190 200 C180 240, 160 280, 140 340 C120 400, 105 460, 95 540 C88 600, 82 680, 78 780 C76 840, 74 870, 72 900" />
                <path d="M168 440 C155 480, 135 510, 115 560 C95 610, 80 670, 68 750 C60 810, 55 850, 50 900" />
                <path d="M140 340 C125 370, 100 400, 80 450 C60 500, 48 560, 40 640 C35 700, 30 780, 28 900" />

                {/* Right branching */}
                <path d="M215 220 C228 260, 250 310, 270 370 C290 430, 302 490, 312 570 C318 630, 325 710, 328 800 C330 850, 332 880, 333 900" />
                <path d="M238 480 C252 520, 272 560, 290 610 C308 660, 320 720, 330 800 C335 850, 340 880, 342 900" />
                <path d="M270 370 C288 410, 310 450, 325 510 C340 570, 350 640, 358 730 C362 790, 365 850, 368 900" />

                {/* Fine tertiary branches */}
                <path d="M115 560 C100 590, 75 630, 55 690 C40 740, 30 800, 25 900" opacity="0.6" />
                <path d="M312 570 C325 610, 345 650, 355 710 C362 760, 370 820, 375 900" opacity="0.6" />
                <path d="M80 450 C65 490, 45 540, 32 610 C22 680, 15 770, 12 900" opacity="0.5" />
                <path d="M325 510 C342 550, 360 600, 370 670 C378 730, 385 810, 388 900" opacity="0.5" />
            </g>
        </svg>
    );
}
