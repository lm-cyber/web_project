import classNames from 'classnames';
import styles from './index.module.scss';
import { IIconProps } from './types';

const cx = classNames.bind(styles);

const Icon = (props: IIconProps) => {
    const { icon, size, color, className, style } = props;
    let width: number | string = 0;

    if (props.width) {
        width = props.width;
    } else {
        switch (size) {
            case 'xs': {
                width = '10px';
                break;
            }
            case 'sm': {
                width = '20px';
                break;
            }
            case 'md': {
                width = '46px';
                break;
            }
            case 'lg': {
                width = '60px';
                break;
            }
            default: {
                width = '20px';
            }
        }
    }

    const baseClassName = styles[`icon-${icon}`];

    return (
        <i
            className={cx(baseClassName, className, styles.icon)}
            style={{
                width,
                height: props.height ?? width,
                backgroundColor: color,
                ...style,
            }}
            onClick={props.onClick}
            onMouseEnter={props.onMouseEnter}
            onMouseLeave={props.onMouseLeave}
        />
    );
};

export default Icon;
