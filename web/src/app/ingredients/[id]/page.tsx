'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import StampLogo from '@/components/StampLogo';
import Nav from '@/components/Nav';
import { getIngredient, getCategoryDisplay } from '@/lib/data';

const ORIGIN_COLORS: Record<string, string> = {
    '한방': '#B85C3A', '과학': '#5B7B8F', '식품': '#7B9E6B',
    '전통': '#8B7355', '아유르베다': '#D4A843',
    '현대과학': '#5B7B8F', '전통한방': '#B85C3A', '전통의학': '#8B7355', '식품유래': '#7B9E6B',
};
const EVIDENCE_MAP: Record<string, number> = { '매우 양호': 4, '양호': 3, '보통': 2, '제한적': 1 };

/** Render text with \n\n as separate paragraphs */
function Paragraphs({ text }: { text: string }) {
    const parts = text.split('\n\n').filter(Boolean);
    return <>{parts.map((p, i) => <p key={i}>{p}</p>)}</>;
}

/** Parse food_sources text into a mini table if it contains parenthetical amounts */
function FoodSourcesTable({ text }: { text: string }) {
    // Try to extract items like "식품명(100g당 ~XX mg)"
    const regex = /([^,，]+?)\s*\(([^)]+)\)/g;
    const entries: { name: string; amount: string }[] = [];
    let match;
    while ((match = regex.exec(text)) !== null) {
        entries.push({ name: match[1].trim(), amount: match[2].trim() });
    }

    if (entries.length >= 3) {
        // Get any trailing text after the last parenthetical
        const lastIdx = text.lastIndexOf(')');
        const trailing = lastIdx !== -1 ? text.slice(lastIdx + 1).replace(/^[,，.\s]+/, '').trim() : '';

        return (
            <>
                <table className="info-table food-sources-table">
                    <thead>
                        <tr><th>식품</th><th>함량</th></tr>
                    </thead>
                    <tbody>
                        {entries.map((e, i) => (
                            <tr key={i}><td>{e.name}</td><td>{e.amount}</td></tr>
                        ))}
                    </tbody>
                </table>
                {trailing && <p style={{ marginTop: '12px' }}>{trailing}</p>}
            </>
        );
    }

    // Fallback to paragraphs
    return <Paragraphs text={text} />;
}

/** Render food_sources_table array as a proper table */
function FoodSourcesSection({ item }: { item: any }) {
    const table = item.food_sources_table;
    const text = item.food_sources;

    if (table && table.length > 0) {
        // Show table-only; skip the old text field (it duplicates the table data)
        return (
            <section className="detail-section">
                <h2>어디서 찾을 수 있나요</h2>
                <table className="info-table food-sources-table">
                    <thead>
                        <tr><th>식품</th><th>함량 (1회 기준)</th></tr>
                    </thead>
                    <tbody>
                        {table.map((row: { food: string; amount: string }, i: number) => (
                            <tr key={i}><td>{row.food}</td><td>{row.amount}</td></tr>
                        ))}
                    </tbody>
                </table>
            </section>
        );
    }

    // Fallback: text-only (for additives, some extracts, etc.)
    if (text) {
        return (
            <section className="detail-section">
                <h2>어디서 찾을 수 있나요</h2>
                <FoodSourcesTable text={text} />
            </section>
        );
    }

    return null;
}

export default function IngredientPage() {
    const params = useParams();
    const id = params.id as string;
    const item = getIngredient(id);


    if (!item) {
        return (
            <div className="container detail-page" style={{ textAlign: 'center', paddingTop: '120px' }}>
                <h1 style={{ fontWeight: 300, marginBottom: 16 }}>원료를 찾을 수 없습니다</h1>
                <Link href="/" style={{ color: '#666', borderBottom: '1px solid #ccc' }}>홈으로 돌아가기</Link>
            </div>
        );
    }

    const originColor = ORIGIN_COLORS[item.origin_type || ''] || '#888';
    const evidenceFilled = EVIDENCE_MAP[item.evidence_level || ''] || 0;

    return (
        <>
            <Nav />

            <div className="container detail-page">
                {/* Breadcrumb */}
                <div className="detail-breadcrumb">
                    <Link href="/">홈</Link>{' / '}
                    <span>{getCategoryDisplay(item.category)}</span>{' / '}
                    <span>{item.name}</span>
                </div>

                {/* Header */}
                <header className="detail-header">
                    <h1 className="detail-title">{item.name}</h1>
                    {item.name_en && <p className="detail-name-en">{item.name_en}</p>}
                    {item.nickname && <p className="detail-nickname">{item.nickname}</p>}
                    <div className="detail-indicators">
                        {item.origin_type && (
                            <div className="origin-indicator">
                                <span className="origin-bar" style={{ backgroundColor: originColor }} />
                                <span>{item.origin_type}</span>
                            </div>
                        )}
                        {item.evidence_level && (
                            <div className="evidence-dots" title="근거 수준">
                                <span className="evidence-prefix">근거 수준</span>
                                {[0, 1, 2, 3].map((i) => (
                                    <span key={i} className={`evidence-dot ${i < evidenceFilled ? 'filled' : 'empty'}`} />
                                ))}
                                <span className="evidence-label">{item.evidence_level}</span>
                            </div>
                        )}
                    </div>
                </header>

                {/* Info table */}
                <section className="detail-section">
                    <h2>기본 정보</h2>
                    <table className="info-table">
                        <tbody>
                            {item.name_en && <tr><td>영문명</td><td>{item.name_en}</td></tr>}
                            {item.aliases && item.aliases.length > 0 && <tr><td>다른 이름</td><td>{item.aliases.join(', ')}</td></tr>}
                            <tr><td>분류</td><td>{getCategoryDisplay(item.category)}</td></tr>
                            {item.source_type && <tr><td>원료 유형</td><td>{item.source_type}</td></tr>}
                            {item.daily_recommended && <tr><td>일일 권장량</td><td>{item.daily_recommended}</td></tr>}
                            {item.upper_limit && <tr><td>상한섭취량</td><td>{item.upper_limit}</td></tr>}
                            {item.dosage_reference && <tr><td>보충 용량</td><td>{item.dosage_reference}</td></tr>}
                        </tbody>
                    </table>
                </section>

                {/* Description — multi-paragraph */}
                {(item.content_description || item.content_brief) && (
                    <section className="detail-section">
                        <h2>이 원료는 뭔가요</h2>
                        <Paragraphs text={item.content_description || item.content_brief} />
                    </section>
                )}

                {/* Origin story — multi-paragraph */}
                {item.origin_story && (
                    <section className="detail-section">
                        <h2>뿌리 — 기원 이야기</h2>
                        <div className="origin-story">
                            <Paragraphs text={item.origin_story} />
                        </div>
                    </section>
                )}

                {/* MFDS */}
                {item.mfds_functionality && (
                    <section className="detail-section">
                        <h2>식약처 인정 기능성</h2>
                        <p className="mfds-quote">{item.mfds_functionality}</p>
                    </section>
                )}

                {/* Food Sources — TABLE */}
                <FoodSourcesSection item={item} />

                {/* Fun fact — multi-paragraph */}
                {item.fun_fact && (
                    <section className="detail-section">
                        <h2>흥미로운 이야기</h2>
                        <div className="fun-fact">
                            <Paragraphs text={item.fun_fact} />
                        </div>
                    </section>
                )}

                {/* Safety — multi-paragraph */}
                {item.safety_class && (
                    <section className="detail-section">
                        <h2>안전성</h2>
                        <Paragraphs text={item.safety_class} />
                    </section>
                )}

                {/* Function tags */}
                {item.tags_function && item.tags_function.length > 0 && (
                    <section className="detail-section">
                        <h2>주요 기능</h2>
                        <div className="tags-row">
                            {item.tags_function.map((fn: string) => <span key={fn} className="tag-link">{fn}</span>)}
                        </div>
                    </section>
                )}

                {/* Related ingredients */}
                {item.related_ingredients && item.related_ingredients.length > 0 && (
                    <section className="detail-section">
                        <h2>같이 알면 좋은 원료</h2>
                        <div className="tags-row">
                            {item.related_ingredients.map((relId: string) => {
                                const rel = getIngredient(relId);
                                return rel ? (
                                    <Link key={relId} href={`/ingredients/${relId}`} className="tag-link">{rel.name}</Link>
                                ) : null;
                            })}
                        </div>
                    </section>
                )}

                {/* Purpose tags */}
                {item.tags_purpose && item.tags_purpose.length > 0 && (
                    <section className="detail-section">
                        <h2>관련 목적</h2>
                        <div className="tags-row">
                            {item.tags_purpose.map((tag: string) => (
                                <Link key={tag} href={`/purpose/${tag}`} className="tag-link">{tag}</Link>
                            ))}
                        </div>
                    </section>
                )}

                {/* References */}
                {item.references && item.references.length > 0 && (
                    <section className="detail-section">
                        <h2>참고 문헌</h2>
                        <ol className="references-list">
                            {item.references.map((ref: string, i: number) => (
                                <li key={i}>{ref}</li>
                            ))}
                        </ol>
                    </section>
                )}
            </div>
        </>
    );
}
