import React, { MouseEventHandler } from 'react';
import classNames from 'classnames';
import { ru } from './i18n/ru.ts';
import styles from './index.module.scss';
import { constants } from '../../../core/constants';
import { AppDispatch } from '../../../core/store/index.ts';
import { store } from '../../../core/store/index.ts';
import { addToCart } from '../../../core/api/cart/index.ts';

interface IProductDetailsProps {
    id: number;
    productName: string;
    description: string;
    img: string;
}
const cx = classNames.bind(styles);

export const CatalogFullItem: React.FC<IProductDetailsProps> = (props) => {
    const dispatch: AppDispatch = store.dispatch;

    const handleAddToCart: MouseEventHandler<HTMLButtonElement> = () => {
        dispatch(
            addToCart({
                id: props.id,
                productName: props.productName,
                images: props.img,
                amount: 0,
            }),
        );
    };

    return (
        <div className={cx(styles.fullItemContainer)}>
            <img
                loading="lazy"
                srcSet={`${constants.imageUrl}${props.img}`}
                className={cx(styles.fullItemImage)}
                alt={'shit'}
            />
            <span className={cx(styles.catalogFullItem)}>
                <div className="flex items-stretch justify-between gap-5">
                    <span className="flex flex-col items-stretch justify-center">
                        <div className={cx(styles.productTitle)}>{props.productName}</div>
                    </span>
                    <button className={cx(styles.toCartButton)} onClick={handleAddToCart}>
                        {ru.to_cart}
                    </button>
                </div>
                <div className={cx(styles.descriptionTitle)}>{ru.description}</div>
                <div className={cx(styles.description)}>{props.description}</div>
            </span>
        </div>
    );
};
