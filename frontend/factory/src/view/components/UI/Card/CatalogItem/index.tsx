import React from 'react';
import classNames from 'classnames';
import { Link } from 'react-router-dom';
import styles from './index.module.scss';
import { constants } from '../../../../../core/constants';

const cx = classNames.bind(styles);

interface ICatalogItemProps {
    id: number;
    title: string;
    imageId: string;
}
export const CatalogItem: React.FC<ICatalogItemProps> = (props) => {
    const title = props.title.length > 30 ? props.title.slice(0, 30).trim() + '...' : props.title;

    return (
        <Link to={`/catalog/${props.id}`}>
            <div className={cx(styles.catalogItem)}>
                <img
                    className={styles.image}
                    src={`${constants.imageUrl}${props.imageId}`}
                    alt={props.imageId.toString()}
                />
                <div className={cx(styles.title)}>{title}</div>
            </div>
        </Link>
    );
};
