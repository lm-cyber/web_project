import React from 'react';
import classNames from 'classnames';
import { Link } from 'react-router-dom';
import { ru } from './i18n/ru.ts';
import styles from './index.module.scss';
import { useGetProductsQuery } from '../../../core/api/product';
import { Title } from '../UI/Text/Title';
import { ContentWrapper } from '../ContentWrapper';
import { CatalogCard } from '../UI/Card/CatalogCard';

const cx = classNames.bind(styles);

export const CatalogPart: React.FC = () => {
    const { data } = useGetProductsQuery();

    return (
        <ContentWrapper>
            <div className={cx(styles.wrapper)}>
                <Title name={ru.title} />
                <div className={cx(styles.scrollable, styles.hideScrollBar)}>
                    <div className={cx(styles.cardsWrapper)}>
                        {data?.slice(0, 7)?.map((product) => (
                            <Link key={product.id} to={`/catalog/${product.id}`}>
                                <CatalogCard key={product?.id} title={product?.name} imageId={product?.images[0]?.id} />
                            </Link>
                        ))}
                    </div>
                </div>
            </div>
        </ContentWrapper>
    );
};
