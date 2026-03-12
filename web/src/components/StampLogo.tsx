export default function StampLogo({ size = 32, className = '' }: { size?: number; className?: string }) {
    return (
        <svg
            width={size}
            height={size}
            viewBox="0 0 100 100"
            className={className}
            xmlns="http://www.w3.org/2000/svg"
            role="img"
            aria-label="뿌리 로고"
        >
            <rect x="2" y="2" width="96" height="96" rx="4" fill="#2C2C2C" />
            {/* 뿌 positioned upper-left diagonal */}
            <text
                x="35" y="40"
                textAnchor="middle"
                dominantBaseline="central"
                fill="#FFFFFF"
                fontFamily="'Pretendard Variable', Pretendard, sans-serif"
                fontWeight="900"
                fontSize="38"
                letterSpacing="-2"
            >
                뿌
            </text>
            {/* 리 positioned lower-right diagonal */}
            <text
                x="65" y="72"
                textAnchor="middle"
                dominantBaseline="central"
                fill="#FFFFFF"
                fontFamily="'Pretendard Variable', Pretendard, sans-serif"
                fontWeight="900"
                fontSize="38"
                letterSpacing="-2"
            >
                리
            </text>
        </svg>
    );
}
