'use client';

import { useState } from 'react';
import Link from 'next/link';
import Nav from '@/components/Nav';

export default function AboutPage() {
    return (
        <>
            <Nav />

            <div className="container detail-page">
                <div className="detail-breadcrumb">
                    <Link href="/">홈</Link> / <span>소개</span>
                </div>

                <header className="detail-header">
                    <h1 className="detail-title" style={{ marginBottom: '8px' }}>뿌리</h1>
                    <p className="detail-nickname">건강기능식품 원료 사전</p>
                </header>

                {/* Intro */}
                <section className="detail-section">
                    <h2>이 사이트에 대해</h2>
                    <p>
                        뿌리는 건강기능식품에 사용되는 원료의 기원과 근거를 추적하는 사전입니다.
                        우리가 매일 섭취하는 비타민, 미네랄, 프로바이오틱스, 약용식물 추출물의 뒷이야기 —
                        어디에서 왔는지, 누가 발견했는지, 과학적으로 어떤 근거가 있는지 — 를 찾아가는 여정입니다.
                    </p>
                    <p>
                        각 원료 페이지에는 기원 이야기, 식약처 인정 기능성, 식품 공급원, 안전성 정보가 포함되어 있습니다.
                        충분한 임상 근거가 있는 원료와 전통적 경험에 기반한 원료를 구분하여 표시하며,
                        소비자가 근거에 기반한 판단을 할 수 있도록 돕는 것이 목표입니다.
                    </p>
                </section>

                {/* How to use */}
                <section className="detail-section">
                    <h2>사용 가이드</h2>
                    <p>
                        홈 화면의 검색창에서 원료명(한글 또는 영문)을 검색하거나,
                        상세 필터(목적, 신체부위, 기원 유형)를 사용하여 원하는 원료를 찾을 수 있습니다.
                    </p>
                    <p>
                        각 원료는 Tier(등급)로 분류됩니다:
                    </p>
                    <table className="info-table">
                        <tbody>
                            <tr><td>T1</td><td>가장 많이 소비되고 연구 근거가 풍부한 핵심 원료 (160종)</td></tr>
                            <tr><td>T2</td><td>전문 영역이나 특정 목적에서 사용되는 원료 (286종)</td></tr>
                            <tr><td>T3</td><td>소규모 연구 또는 전통적 사용 근거만 있는 원료 (116종)</td></tr>
                        </tbody>
                    </table>
                </section>

                {/* Evidence legend — 표시안내 moved here */}
                <section className="detail-section">
                    <h2>표시 안내</h2>

                    <h3 style={{ fontSize: '15px', fontWeight: 500, marginBottom: '12px', marginTop: '24px' }}>근거 수준</h3>
                    <p style={{ marginBottom: '16px' }}>연구 결과의 양과 질을 4단계로 요약합니다.</p>
                    <table className="info-table">
                        <tbody>
                            <tr><td style={{ whiteSpace: 'nowrap' }}>●●●●</td><td><strong>매우 양호</strong> — 다수의 대규모 임상시험에서 일관되게 확인된 효과</td></tr>
                            <tr><td style={{ whiteSpace: 'nowrap' }}>●●●○</td><td><strong>양호</strong> — 복수의 연구에서 일관된 결과가 보고됨</td></tr>
                            <tr><td style={{ whiteSpace: 'nowrap' }}>●●○○</td><td><strong>보통</strong> — 연구 결과가 있으나 규모나 수가 제한적</td></tr>
                            <tr><td style={{ whiteSpace: 'nowrap' }}>●○○○</td><td><strong>제한적</strong> — 예비 연구 또는 전통적 사용 근거</td></tr>
                        </tbody>
                    </table>

                    <h3 style={{ fontSize: '15px', fontWeight: 500, marginBottom: '12px', marginTop: '32px' }}>기원 유형</h3>
                    <p style={{ marginBottom: '16px' }}>원료가 처음 발견되거나 사용된 맥락을 표시합니다.</p>
                    <table className="info-table">
                        <tbody>
                            <tr><td><span style={{ display: 'inline-block', width: 12, height: 12, borderRadius: 2, background: '#5B7B8F', marginRight: 8, verticalAlign: 'middle' }} />현대과학</td><td>현대 약리학·생화학 연구를 통해 발견·규명된 원료</td></tr>
                            <tr><td><span style={{ display: 'inline-block', width: 12, height: 12, borderRadius: 2, background: '#B85C3A', marginRight: 8, verticalAlign: 'middle' }} />전통한방</td><td>한의학 처방에서 유래한 원료</td></tr>
                            <tr><td><span style={{ display: 'inline-block', width: 12, height: 12, borderRadius: 2, background: '#8B7355', marginRight: 8, verticalAlign: 'middle' }} />전통의학</td><td>아유르베다, 유럽 약초학 등 전통 의학에서 유래</td></tr>
                            <tr><td><span style={{ display: 'inline-block', width: 12, height: 12, borderRadius: 2, background: '#7B9E6B', marginRight: 8, verticalAlign: 'middle' }} />식품유래</td><td>일반 식품에서 유효 성분을 추출·농축한 원료</td></tr>
                            <tr><td><span style={{ display: 'inline-block', width: 12, height: 12, borderRadius: 2, background: '#D4A843', marginRight: 8, verticalAlign: 'middle' }} />아유르베다</td><td>인도 전통 의학 아유르베다에서 유래한 원료</td></tr>
                        </tbody>
                    </table>
                </section>

                {/* Disclaimer */}
                <section className="detail-section">
                    <h2>면책 사항</h2>
                    <p style={{ color: '#999', fontSize: '13px', lineHeight: 1.8 }}>
                        본 사이트의 정보는 참고용이며, 의학적 진단이나 치료를 대체하지 않습니다.
                        건강기능식품의 섭취는 전문가와 상담 후 결정하시기 바랍니다.
                        본 사이트에 수록된 정보는 최신 연구를 반영하기 위해 주기적으로 업데이트됩니다.
                    </p>
                </section>
            </div>
        </>
    );
}
