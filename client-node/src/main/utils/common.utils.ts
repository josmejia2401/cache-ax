export class CommonUtil {
    static parse(value: any) {
        try {
            return JSON.parse(value);
        } catch (error) { }
        return value;
    }
}